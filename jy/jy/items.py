# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JyItem(scrapy.Item):
     #类型
     type = scrapy.Field()
     #标题
     title = scrapy.Field()
     #简介
     content = scrapy.Field()
     #工具原料1
     tool1 = scrapy.Field()
     #工具原料2
     tool2 = scrapy.Field()
     #步骤1
     image = scrapy.Field()
     #注意事项1
     note1= scrapy.Field()
     #注意事项2
     note2 = scrapy.Field()