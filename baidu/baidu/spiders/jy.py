# -*- coding: utf-8 -*-
import scrapy
from googletrans import Translator

class JySpider(scrapy.Spider):

    name = "jy"
    start_urls = [
        'https://www.howtogeek.com/t/essentials/',
    ]
    def parse(self, response):
        # follow links to author pages
        # follow pagination links
        for href in response.xpath('//h2/a/@href'):
            yield response.follow(href, self.parse_jy)



    def parse_jy(self, response):
        jy =  response.xpath('//div[@class="entry-content e-content"]')
        a = jy.xpath('string(./h2)').extract_first()
        translate = Translator()
        result = translate.translate('hello', dest='zh-CN')
        print ('呵呵呵呵呵呵',result.text)
        k = response.xpath('//div[@class="content-area"]')
        yield {
            'type': jy.xpath('string(./h2)').extract_first(),
            'title': jy.xpath('string(./h2)').extract_first(),
            'summary': jy.xpath('string(./h2)').extract_first(),
            'tool1': jy.xpath('string(./h2)').extract_first(),
            'tool2': jy.xpath('string(./h2)').extract_first(),
            'step1': jy.xpath('string(./h2)').extract_first(),
            'stepimg1': jy.xpath('string(./h2)').extract_first(),
            'step2': jy.xpath('string(./h2)').extract_first(),
            'stepimg2': jy.xpath('string(./h2)').extract_first(),
            'step3': jy.xpath('string(./h2)').extract_first(),
            'stepimg3': jy.xpath('string(./h2)').extract_first(),
            'step4': jy.xpath('string(./h2)').extract_first(),
            'stepimg4': jy.xpath('string(./h2)').extract_first(),
            'step5': jy.xpath('string(./h2)').extract_first(),
            'stepimg5': jy.xpath('string(./h2)').extract_first(),
            'note1': jy.xpath('string(./h2)').extract_first(),
            'note2': jy.xpath('string(./h2)').extract_first(),
        }
		

