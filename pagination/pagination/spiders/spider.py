
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.amazon.cn/gp/bestsellers/books/ref=sv_b_3',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@id="zg-center-div"]'):
            yield {

                'a': quote.xpath('.//a/div/text()').extract(),
                'text': quote.xpath('.//img/@src').extract(),
               
            }

        next_page = response.xpath('.//li[@class="a-last"]/a/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse) 