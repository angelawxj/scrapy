# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        'https://www.amazon.cn/gp/bestsellers/books/ref=sv_b_3',
    ]

    def parse(self, response):
        for amazon in response.xpath('//div[@class="a-section a-spacing-small"]'):
           yield {
                'image_urls': [amazon.xpath('.//img/@src').extract_first()],
            }



