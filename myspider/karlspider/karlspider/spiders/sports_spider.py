#coding=utf-8
'''
Created on 2014年1月25日

@author: karl
'''
import crawl_api
from karlspider.data_manage.data_option import DataOptionGet
from scrapy.spider import BaseSpider

class SportSpider(BaseSpider):
    name = "sportspider.org"
    allowed_domains = ["sportspider.org"]
    start_urls = ['http://www.chinanews.com/sports.shtml']
    def parse(self, response):
        crawl_api.Crawl_Sport_Title(response)
        
        
class SportContentSpider(BaseSpider):
    name = "sportcontentspider.org"
    allowed_domains = ["sportcontentspider.org"]
    start_urls = []
    dataoptionget = DataOptionGet()
    mission = dataoptionget.get_Unlock_Links_Sport()
    num = len(mission)
    for i in range(num):
        start_urls.append(mission[i].link)
    def parse(self,response):
        crawl_api.Crawl_Sport_Content(response)
