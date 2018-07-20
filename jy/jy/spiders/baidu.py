# -*- coding: utf-8 -*-
import scrapy
from googletrans import Translator

class BaiduSpider(scrapy.Spider):

    name = "jy"
    start_urls = [
        'https://www.techradar.com/how-to/mobile-computing/laptops/',
    ]
    def parse(self, response):
        # follow links to author pages
        # follow pagination links
        for href in response.xpath('//div[@class="listingResult small"]/a/@href'):
            yield response.follow(href, self.parse_jy)

        # next_page = response.xpath('//span[@class="next"]/a/@href').extract_first()
        # if next_page is not None:
            # yield response.follow(next_page, callback=self.parse) 

    def parse_jy(self, response):
        t = response.xpath('//header/h1')
        c = response.xpath('//div[@id="article-body"]/p')
        img = response.xpath('//div[@id="article-body"]/h3')
        #标题
        title = t.xpath('string(.)').extract_first()
        #简介
        content = str(c.xpath('string(.)').extract())
        #步骤
        image = str(img.xpath('string(.)').extract())

        translator = Translator(service_urls=[
            'translate.google.cn',
        ])
        translator.translate('hello', dest='zh-CN').text
        yield {
            'type': '笔记本',
            'title': translator.translate(title, dest='zh-CN').text,
            'content':translator.translate(content, dest='zh-CN').text,
            'tool1': '电脑',
            'tool2': '系统，软件',
            'image': '',
            'note1': '针对不同的问题，不同处理',
            'note2': '你的点赞是我写经验的动力',
        }
		
		
		
		
		
		
		
		
		
		