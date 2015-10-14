from bs4 import BeautifulSoup as bs
from scrapy.http import Request
from scrapy.spider import BaseSpider
from hn.items import HnItem


class HnSpider(BaseSpider):
    name = 'hn'
    allowed_domains = []
    start_urls = ['http://news.163.com',
                    "http://news.qq.com",
                    "http://news.baidu.com",]

    def parse(self, response):
        if 'news.163.com' in response.url:
            soup = bs(response.body)
            items = [(y[0].get_text(),y[0].get("href")) for y in 
            filter (None,[x for x in soup.find_all('a',{'class':'ns-wnews mb40'})])]

            for item in items:
                print item

                hn_item = HnItem()
                hn_item['title'] = item[0]
                hn_item['link'] = item[1]
                try:
                    yield Request(item[1], callback=self.parse)
                except ValueError:
                    yield Request('http://news.163.com/' + item[1], callback=self.parse)

                yield hn_item

