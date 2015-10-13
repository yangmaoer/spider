# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log,signals
from twisted.enterprise import adbapi
from scrapy.http import Request
import json,codecs
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
import time
import re,datetime
from hashlib import md5
import MySQLdb,MySQLdb.cursors
from netease.items import NeteaseItem



# class JsonWithEncodingNeteasePipeline(object):
#     def __init__(self):
#     self.file = codecs.open('news163.json', 'w', encoding='utf-8')
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.file.write(line)
#     return item
#     def spider_closed(self, spider):
#         self.file.close()

class NeteasePipeline(object):
	def __init__(self):
		self.dbpool = dbpool

	@classmethod
	def form_settings(cls,settings):
		dbargs = dict(
			host = settings['MYSQL_HOST'],
			db = settings["MYSQL_DBNAME"],
			user = settings['MYSQL_USER'],
			passwd = settings['MYSQL_PASSWD'],
			charset  = 'utf8',
			cursorclass = MySQLdb.cursors.DictCursor,
			use_unicode = True,
			)
		dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)
		return cls(dbpool)

    	def process_item(self, item, spider):
        		query = self.dbpool.runInteraction(self._conditional_insert, item,spider)
        		query.addErrback(self.handle_error,item,spider)
        		query.addBoth(lambda _: item)

        		return query

        	def _conditional_insert(self,conn,item):
        		linkmd5id = self._get_linkmd5id(item)
        		now = datetime.utcnow().replace(microsecond = 0).isoformat(' ')
        		conn.execute("""
        			select * from  content where linkmd5id = %s""",(linkmd5id,))
        		ret = conn.fetchone()

        		if ret:
        			conn.execute("""
        				update content set title = %s,description = %s,link = %s, listUrl = %s, updated = %s ,picUrl = %s where linkmd5id = %s""",
        				(item['title'], item['desc'], item['link'], item['listUrl'], now, item["picUrl"]linkmd5id))
        		else:
        			conn.execute("""
        				insert into cnblogsinfo(linkmd5id, title, description, link, listUrl, updated,picUrl) values(%s, %s, %s, %s, %s, %s,%s)""",
		 		(linkmd5id, item['title'], item['desc'], item['link'], item['listUrl'], now,item['picUrl']))

        	def _get_linkmd5id(self,item):
        		return md5(item['link']).hexdigest()

        	def _handle_error(self,failue,item):
        		log.err(failue)