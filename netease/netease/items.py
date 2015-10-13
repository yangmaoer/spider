# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NeteaseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	title = scrapy.Field()
	linkmd5id = scrapy.Field()
	link = scrapy.Field()
	desc = scrapy.Field()
	linkUrl = scrapy.Field()
	picUrl = scrapy.Field()
