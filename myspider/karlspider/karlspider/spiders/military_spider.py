#coding=utf-8
'''
Created on 2014年1月25日

@author: karl
'''
import crawl_api
from karlspider.data_manage.data_option import DataOptionGet
from scrapy.spider import BaseSpider

class MaliSpider(BaseSpider):
    name = "malispider.org"
    allowed_domains = ["malispider.org"]
    start_urls = ['http://www.chinanews.com/mil/news.shtml']
    def parse(self, response):
        crawl_api.Crawl_Malitary_Title(response)
        
        
class MaliContentSpider(BaseSpider):
    name = "malicontentspider.org"
    allowed_domains = ["malicontentspider.org"]
    start_urls = []
    dataoptionget = DataOptionGet()
    mission = dataoptionget.get_Unlock_Links_MA()
    num = len(mission)
    for i in range(num):
        start_urls.append(mission[i].link)
    def parse(self,response):
        crawl_api.Crawl_Malitary_Content(response)
