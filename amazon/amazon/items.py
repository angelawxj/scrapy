# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
     #书名
     name = scrapy.Field()
     # #作者
     author = scrapy.Field()
     # #封面
     img_url = scrapy.Field()
