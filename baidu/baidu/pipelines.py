# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql
from scrapy import log
from twisted.enterprise import adbapi
from baidu import settings
from baidu.items import BaiduItem
import time

class BaiduPipeline(object):
    # 打开数据库
    def open_spider(self, spider):
        self.db_conn =pymysql.connect(host='127.0.0.1', port=3306, db='baidu', user='root', passwd='dong1990', charset='utf8')
        self.db_cur = self.db_conn.cursor()

    # 关闭数据库
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    # 对数据进行处理
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    #插入数据
    def insert_db(self, item):
        print("哈哈哈",item)
        values = (
            item['type'],
            item['title'],
            item['summary'],
            item['tool1'],
            item['tool2'],
            item['steptitle1'],
            item['step1'],
            item['stepimg1'],
            item['steptitle2'],
            item['step2'],
            item['stepimg2'],
            item['steptitle3'],
            item['step3'],
            item['stepimg3'],
            item['steptitle4'],
            item['step4'],
            item['stepimg4'],
            item['steptitle5'],
            item['step5'],
            item['stepimg5'],
            item['steptitle6'],
            item['step6'],
            item['stepimg6'],
            item['steptitle7'],
            item['step7'],
            item['stepimg7'],
            item['note1'],
            item['note2'],
        )

        sql = 'INSERT INTO books(type,title,summary,tool1,tool2,steptitle1,step1,stepimg1,steptitle2,step2,stepimg2,steptitle3,step3,stepimg3,steptitle4,step4,stepimg4,steptitle5,step5,stepimg5,steptitle6,step6,stepimg6,steptitle7,step7,stepimg7,note1,note2) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self.db_cur.execute(sql, values)