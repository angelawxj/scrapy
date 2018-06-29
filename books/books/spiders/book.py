# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://kgbook.com']

    def parse(self, response):
        # follow links to author pages
        # follow pagination links
        for href in response.xpath('//body/div/div/ul/li/a/@href'):
            yield response.follow(href, self.parse_author)

    def parse_author(self, response):
        for amazon in response.xpath('//div[@class="channel-item"]/div/h3/a/@href'):
            yield response.follow(amazon, self.parse_book)

        next_page = response.xpath('.//div[@class="pagenavi"]/a[last()-1]/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_author) 

    def parse_book(self, response):
        for book in response.xpath('//a[@class="button"]'):
            yield {
                'file_urls': [book.xpath('./@href').extract_first()],
                'file_name': book.xpath('../../h1[@class="news_title"]/text()').extract_first(),
                'folder_name': book.xpath('../../../nav/a[last()]/text()').extract_first(),
            }