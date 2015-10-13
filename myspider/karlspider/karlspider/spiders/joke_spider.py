#coding=utf-8
'''
Created on 2014年1月25日

@author: karl
'''
import crawl_api
from scrapy.spider import BaseSpider

class JokeSpider(BaseSpider):
    name = "jokespider.org"
    allowed_domains = ["jokespider.org"]
    start_urls = ['http://www.budejie.com/duanzi/']
#     for i in range(2000):
#         start_urls.append('http://www.budejie.com/xcs.php?page='+str(i)+'&maxid=1381126801')
    def parse(self, response):
        crawl_api.Crawl_Joke_Content(response)
