# -*- coding: utf-8 -*-
import scrapy

class JySpider(scrapy.Spider):

    name = "jy"
    start_urls = [
        'https://www.howtogeek.com/page/2/',
    ]
    def parse(self, response):
        # follow links to author pages
        # follow pagination links
        for href in response.xpath('//h2/a/@href'):
            yield response.follow(href, self.parse_jy)



    def parse_jy(self, response):
        jy =  response.xpath('//div[@class="entry-content e-content"]')
        t = response.xpath('//div[@id="primary"]/main/article/header/a')
        #标题
        title = t.xpath('string(.)').extract_first()
        a = t.xpath('string(.)').extract_first()
        #步骤
        # steptitle1 = jy.xpath('string(./h2)').extract_first()
        # step1 = jy.xpath('string(./h2/following-sibling::p[1])').extract_first()
        # stepimg1 = jy.xpath('string(./h2/following-sibling::p[1])').extract_first()

        # steptitle2 = jy.xpath('string(./h2)').extract_first()
        # step2 = jy.xpath('string(./h2[2])').extract_first()
        # stepimg2 = jy.xpath('string(./h2[2])').extract_first()

        # steptitle3 = jy.xpath('string(./h2)').extract_first()
        # step3 = jy.xpath('string(./h2[3])').extract_first()
        # stepimg3 = jy.xpath('string(./h2[3])').extract_first()
		
        # steptitle4 = jy.xpath('string(./h2)').extract_first()
        # step4 = jy.xpath('string(./h2[4])').extract_first()
        # stepimg4 = jy.xpath('string(./h2[4])').extract_first()

        # steptitle5 = jy.xpath('string(./h2)').extract_first()
        # step5 = jy.xpath('string(./h2[5])').extract_first()
        # stepimg5 = jy.xpath('string(./h2[5])').extract_first()

        yield {
            'type': a,
            'title': title,
            'summary':a,
            'tool1': a,
            'tool2': a,
            'steptitle1': a,
            'step1': a,
            'stepimg1': a,
            'steptitle2': a,
            'step2': a,
            'stepimg2': a,
            'steptitle3': a,
            'step3': a,
            'stepimg3': a,
            'steptitle4': a,
            'step4': a,
            'stepimg4': a,
            'steptitle5': a,
            'step5': a,
            'stepimg5': a,
            'note1': a,
            'note2': a,
        }
		
