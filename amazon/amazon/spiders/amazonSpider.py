# -*- coding: utf-8 -*-
import scrapy


class AmazonspiderSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
        'https://www.amazon.cn/gp/bestsellers/books/ref=sv_b_3',
    ]

    def parse(self, response):
        for amazon in response.xpath('//div[@class="zg_itemRow"]'):
           yield {
                'name': amazon.xpath('.//img/@alt').extract_first(),
                'author': amazon.xpath('.//span[@class="a-size-small a-color-base"]/text()').extract_first(),
                'img_url': amazon.xpath('.//img/@src').extract_first(),
            }
            



