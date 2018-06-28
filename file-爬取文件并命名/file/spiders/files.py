# -*- coding: utf-8 -*-
import scrapy


class FilesSpider(scrapy.Spider):
    name = 'files'
    start_urls = [
        'https://kgbook.com',
    ]

    def parse(self, response):
        for amazon in response.xpath('//a[@class="button"]'):
           yield {
                'file_urls': [amazon.xpath('./@href').extract_first()],
                'file_name': amazon.xpath('../../h1[@class="news_title"]/text()').extract_first(),
            }
