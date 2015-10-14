#coding:utf-8
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
from netease.items import NeteaseItem
import time
class ExampleSpider(CrawlSpider):
    name = "news"
    allowed_Domains = ["news.163.com"]
    start_urls = ['http://news.163.com/']
    rules = [
        Rule(LinkExtractor(allow=r"/15/\d+/\d+/*"),
        'parse_news')
    ]

def parse_news(self,response):
    items = []
    news = NeteaseItem()
    news['newsTitle'] = response.xpath("//*[@id=\"h1title\"]/text()").extract()
    news['newsSourceUrl'] = response.xpath("//*[@id=\"ne_article_source\"]/a/@href").extract()
    news['newsComment'] = response.xpath("//p/text()").extract()
    news['picUrl'] = response.xpath("//*[contains(@href,\"img1\") ]/img/@src").extract()
    #         item['picdesc'] = response.xpath('//*[contains(@href,"img1") ]/img/@alt').extract()
    #         #print item['title'] + "***************\r\n"
    # item['newsUrl'] = response.css('a').xpath('//*[@id=\"ne_article_source\"]/@href').extract()
    #         item['newsComment'] = response.xpath('//*[@id = \"endText\"]/text()').extract()
    #         item['picUrl'] = postTitle[index].xpath("//*[@id= \"ns-gally-con UI_GALLERY_CON\"]/img/@src").extract()
    news["newsTime"] =int(1000 * time.time())
    items.append(news)
    print items
    return items