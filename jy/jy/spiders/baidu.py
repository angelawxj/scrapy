# -*- coding: utf-8 -*-
# from selenium import webdriver  //添加自动化selenium,未完成
import scrapy
from googletrans import Translator
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
from jy.a import ajson

class BaiduSpider(scrapy.Spider):
    name = "kj"
    start_urls = [
        'https://www.healthline.com',
    ]
    def parse(self, response):
        scrapy.Request("https://www.healthline.com/api/nutrition/feed?rows=131&start=1")
        print ("哈哈哈哈或或或或或或或或或", ajson)
                                   

        for jy in response.xpath("//li[@class='css-8wnrqm']/div/div/a/h2") :
            yield {
                'type': '笔记本',
                'title': jy.xpath('string(.)').extract_first(),
                'content':'',
                'tool1': '电脑',
                'tool2': '系统，软件',
                'image': '',
                'note1': '针对不同的问题，不同处理',
                'note2': '你的点赞是我写经验的动力',
            }

        # next_page = response.xpath('//span[@class="next"]/a/@href').extract_first()
        # if next_page is not None:
            # yield response.follow(next_page, callback=self.parse) 

    # def parse_jy(self, response):
        # t = response.xpath('//h1')
        # c = response.xpath('//div[@id="article-body"]/p')
        # img = response.xpath('//div[@id="article-body"]/h3')
        # #标题
        # title = t.xpath('string(.)').extract_first()
        # #简介
        # content = str(c.xpath('string(.)').extract())
        # #步骤
        # image = str(img.xpath('string(.)').extract())

        # translator = Translator(service_urls=[
            # 'translate.google.cn',
        # ])
        # translator.translate('hello', dest='zh-CN').text
        # yield {
            # 'type': '笔记本',
            # 'title': translator.translate(title, dest='zh-CN').text,
            # 'content':translator.translate(content, dest='zh-CN').text,
            # 'tool1': '电脑',
            # 'tool2': '系统，软件',
            # 'image': '',
            # 'note1': '针对不同的问题，不同处理',
            # 'note2': '你的点赞是我写经验的动力',
        # }

# #添加自动化selenium,未完成
# class BaiduSpider(scrapy.Spider):
    # name = "jy"
    # start_urls = [
        # 'https://www.healthline.com/nutrition',
    # ]
    # path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    # print("哈哈哈哈或或或或或或或或或11111110000000000",path)
    # driver = webdriver.Chrome(executable_path=path)
    # print("哈哈哈哈或或或或或或或或或1111111",path)
    # driver.get("https://www.baidu.com")
    # time.sleep(100)
    # driver.get("https://www.healthline.com/nutrition")
    # print("哈哈哈哈或或或或或或或或或222222222",path)
    # time.sleep(100)
    # for _ in range(5):
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        # driver.implicitly_wait(10)  # 隐性等待,最长10秒
    # def parse(self, response):
        # data = self.driver.find_element_by_xpath("//li[@class='css-8wnrqm']/div/div/a/@href") 
        # print("哈哈哈哈或或或或或或或或或ddddddddd",data)
        # for jy in self.driver.find_element_by_xpath("//li[@class='css-8wnrqm']/div/div/a/h2"):
            # yield {
                # 'type': '笔记本',
                # 'title': jy.xpath('string(.)').extract_first(),
                # 'content':'',
                # 'tool1': '电脑',
                # 'tool2': '系统，软件',
                # 'image': '',
                # 'note1': '针对不同的问题，不同处理',
                # 'note2': '你的点赞是我写经验的动力',
            # }