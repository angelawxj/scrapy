# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql
from scrapy import log
from twisted.enterprise import adbapi
from amazon import settings
from amazon.items import AmazonItem
import time
 


class AmazonPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.csv ', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
		


class MysqlPipeline(object):

    # 打开数据库
    def open_spider(self, spider):
        self.db_conn =pymysql.connect(host='127.0.0.1', port=3306, db='amazon', user='root', passwd='dong1990', charset='utf8')
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
            item['name'],
            item['author'],
            item['img_url'],
        )

        sql = 'INSERT INTO books(name,author,img_url) VALUES(%s,%s,%s)'
        self.db_cur.execute(sql, values)