#coding=utf-8
'''
Created on 2014年1月25日

@author: karl
'''
import crawl_api
from karlspider.data_manage.data_option import DataOptionGet
from scrapy.spider import BaseSpider

class EntertainmentSpider(BaseSpider):
    name = "entertainmentspider.org"
    allowed_domains = ["entertainmentspider.org"]
    start_urls = ['http://ent.sina.com.cn/star/']
    def parse(self, response):
        crawl_api.Crawl_Entertainment_Title(response)
        
        
class EntertainmentContentSpider(BaseSpider):
    name = "entertainmentcontentspider.org"
    allowed_domains = ["entertainmentcontentspider.org"]
    start_urls = []
    dataoptionget = DataOptionGet()
    mission = dataoptionget.get_Unlock_Links_ET()
    num = len(mission)
    for i in range(num):
        start_urls.append(mission[i].link)
    def parse(self,response):
        crawl_api.Crawl_Entertainment_Content(response)
