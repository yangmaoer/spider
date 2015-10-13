#coding:utf-8
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
from netease.items import NeteaseItem
class ExampleSpider(CrawlSpider):
    name = "news"
    allowed_Domains = ["news.163.com"]
    start_urls = ['http://news.163.com/']
    rules = [
        Rule(LinkExtractor(allow=r"/15/10\d+/\d+/*"),
        'parse_news')
    ]

def parse_news(self,response):
    items = []
    news = NeteaseItem()
    news['title'] = response.xpath("//*[@id=\"h1title\"]/text()").extract()
    news['linkUrl'] = response.xpath("//*[@id=\"ne_article_source\"]/a/@href").extract()
    news['desc'] = response.xpath("//*[@id=\"endText\"]/text()").extract()
    news['picUrl'] = response.xpath("//*[@id = \"ns-gallery-con UI_GALLERY_CON\"]/img/@src").extract()
    news['link'] = response.url
    items.append(news)
    return items