#coding=utf-8
'''
Created on 2014年1月25日

@author: karl
'''
import crawl_api
from karlspider.data_manage.data_option import DataOptionGet
from scrapy.spider import BaseSpider

class CommunitySpider(BaseSpider):
    name = "communityspider.org"
    allowed_domains = ["communityspider.org"]
    start_urls = ['http://gongyi.ifeng.com/rt-channel/rtlist_0/index.shtml']
    def parse(self, response):
        crawl_api.Crawl_Community_Title(response)
        
        
class CommunityContentSpider(BaseSpider):
    name = "communitycontentspider.org"
    allowed_domains = ["communitycontentspider.org"]
    start_urls = []
    dataoptionget = DataOptionGet()
    mission = dataoptionget.get_Unlock_Links_CO()
    num = len(mission)
    for i in range(num):
        start_urls.append(mission[i].link)
    def parse(self,response):
        crawl_api.Crawl_Community_Content(response)
    
