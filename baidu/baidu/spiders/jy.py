# -*- coding: utf-8 -*-
import scrapy
from googletrans import Translator

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

        next_page = response.xpath('//div[@class="post-navigation"]/div/ul/li/a[@class="next page-numbers"]/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse) 

    def parse_jy(self, response):
        jy = response.xpath('//div[@class="entry-content e-content"]/div/preceding-sibling::p[2]')
        s = response.xpath('//div[@class="entry-content e-content"]/p[2]')
        t = response.xpath('//div[@id="primary"]/main/article/header/a')
        st = response.xpath('//div[@class="entry-content e-content"]')
        # step = st.xpath('//h2[1]/following-sibling::p[1] | following-sibling::p[2]')
        #标题
        title = t.xpath('string(.)').extract_first()
        #简介
        summary = s.xpath('string(.)').extract_first()
        #步骤
        steptitle1 = st.xpath('string(./h2[1])').extract_first()
        step1 = st.xpath('string(.//h2[1]/following-sibling::p[1])').extract_first()
        stepimg1 = st.xpath('.//h2[1]/following-sibling::p[1]/img/@src').extract_first()

        steptitle2 = st.xpath('string(./h2[2])').extract_first()
        step2 = st.xpath('string(.//h2[2]/following-sibling::p[1])').extract_first()
        stepimg2 = st.xpath('.//h2[2]/following-sibling::p[1]/img/@src').extract_first()

        steptitle3 = st.xpath('string(./h2[3])').extract_first()
        step3 = st.xpath('string(.//h2[3]/following-sibling::p[1])').extract_first()
        stepimg3 = st.xpath('.//h2[3]/following-sibling::p[1]/img/@src').extract_first()
		
        steptitle4 = st.xpath('string(./h2[4])').extract_first()
        step4 = st.xpath('string(.//h2[4]/following-sibling::p[1])').extract_first()
        stepimg4 = st.xpath('.//h2[4]/following-sibling::p[1]/img/@src').extract_first()

        steptitle5 = st.xpath('string(./h2[5])').extract_first()
        step5 = st.xpath('string(.//h2[5]/following-sibling::p[1])').extract_first()
        stepimg5 = st.xpath('.//h2[5]/following-sibling::p[1]/img/@src').extract_first()
        translator = Translator(service_urls=[
            'translate.google.cn',
        ])
        translator.translate('hello', dest='zh-CN').text
        yield {
            'type': '游戏',
            'title': translator.translate(title, dest='zh-CN').text,
            'summary':translator.translate(summary, dest='zh-CN').text,
            'tool1': '笔记本电脑',
            'tool2': '软件',
            'steptitle1': translator.translate(steptitle1, dest='zh-CN').text,
            'step1': translator.translate(step1, dest='zh-CN').text,
            'stepimg1':stepimg1,
            'steptitle2': translator.translate(steptitle2, dest='zh-CN').text,
            'step2': translator.translate(step2, dest='zh-CN').text,
            'stepimg2': stepimg2,
            'steptitle3': translator.translate(steptitle3, dest='zh-CN').text,
            'step3': translator.translate(step3, dest='zh-CN').text,
            'stepimg3': stepimg3,
            'steptitle4': translator.translate(steptitle4, dest='zh-CN').text,
            'step4': translator.translate(step4, dest='zh-CN').text,
            'stepimg4': stepimg4,
            'steptitle5': translator.translate(steptitle5, dest='zh-CN').text,
            'step5': translator.translate(step5, dest='zh-CN').text,
            'stepimg5': stepimg5,
            'note1': '谢谢观看本篇经验',
            'note2': '你的点赞是我写经验的动力',
        }
		
