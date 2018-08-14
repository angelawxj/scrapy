# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduItem(scrapy.Item):
     #类型
     type = scrapy.Field()
     #标题
     title = scrapy.Field()
     #简介
     summary = scrapy.Field()
     #工具原料1
     tool1 = scrapy.Field()
     #工具原料2
     tool2 = scrapy.Field()
     #步骤1
     step1 = scrapy.Field()
     steptitle1 = scrapy.Field()
     stepimg1 = scrapy.Field()
     #步骤2
     step2 = scrapy.Field()
     steptitle2 = scrapy.Field()
     stepimg2 = scrapy.Field()
     #步骤3
     step3= scrapy.Field()
     steptitle3 = scrapy.Field()
     stepimg3 = scrapy.Field()
     #步骤4
     step4= scrapy.Field()
     steptitle4 = scrapy.Field()
     stepimg4 = scrapy.Field()
     #步骤5
     step5= scrapy.Field()
     steptitle5 = scrapy.Field()
     stepimg5 = scrapy.Field()
     #步骤6
     step6= scrapy.Field()
     steptitle6 = scrapy.Field()
     stepimg6 = scrapy.Field()
     #步骤7
     step7= scrapy.Field()
     steptitle7 = scrapy.Field()
     stepimg7 = scrapy.Field()
     #注意事项1
     note1= scrapy.Field()
     #注意事项2
     note2 = scrapy.Field()