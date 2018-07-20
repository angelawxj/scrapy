# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
from scrapy import log
from twisted.enterprise import adbapi
from jy import settings
from jy.items import JyItem
import time

class JyPipeline(object):
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
            item['content'],
            item['tool1'],
            item['tool2'],
            item['image'],
            item['note1'],
            item['note2'],
        )

        sql = 'INSERT INTO jy(type,title,content,tool1,tool2,image,note1,note2) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        self.db_cur.execute(sql, values)
