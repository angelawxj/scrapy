# -*- coding: utf-8 -*-
import scrapy


class FilesSpider(scrapy.Spider):
    name = 'files'
    start_urls = [
        'https://kgbook.com/waiguowenxue/1378.html',
    ]

    def parse(self, response):
        for amazon in response.xpath('//a[@class="button"]'):
           yield {
                'file_urls': [amazon.xpath('./@href').extract_first()],
            }