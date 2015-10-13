#coding=utf-8
'''
Created on 2014年1月25日

@author: karl
'''
import crawl_api
from karlspider.data_manage.data_option import DataOptionGet
from scrapy.spider import BaseSpider

class InterSpider(BaseSpider):
    name = "interspider.org"
    allowed_domains = ["interspider.org"]
    start_urls = ['http://news.qq.com/world_index.shtml']
    def parse(self, response):
        crawl_api.Crawl_Inter_Title(response)
        
        
class InterContentSpider(BaseSpider):
    name = "intercontentspider.org"
    allowed_domains = ["intercontentspider.org"]
    start_urls = []
    dataoptionget = DataOptionGet()
    mission = dataoptionget.get_Unlock_Links_IN()
    num = len(mission)
    for i in range(num):
        start_urls.append(mission[i].link)
    def parse(self,response):
        crawl_api.Crawl_Inter_Content(response)
    
