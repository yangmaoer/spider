#coding=utf-8
'''
Created on 2014年1月25日

@author: karl
'''
import crawl_api
from karlspider.data_manage.data_option import DataOptionGet
from scrapy.spider import BaseSpider

class ChinaSpider(BaseSpider):
    name = "chinaspider.org"
    allowed_domains = ["chinaspider.org"]
    start_urls = ['http://news.qq.com/china_index.shtml']
    def parse(self, response):
        crawl_api.Crawl_China_Title(response)
        
        
class ChinaContentSpider(BaseSpider):
    name = "chinacontentspider.org"
    allowed_domains = ["chinacontentspider.org"]
    start_urls = []
    dataoptionget = DataOptionGet()
    mission = dataoptionget.get_Unlock_Links_CH()
    num = len(mission)
    for i in range(num):
        start_urls.append(mission[i].link)
    def parse(self,response):
        crawl_api.Crawl_China_Content(response)
        
