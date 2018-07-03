# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class Bokep2017Spider(scrapy.Spider):
    name = 'bokep2017'
    allowed_domains = ['165.227.89.231']
    start_urls = ['http://165.227.89.231/']
    
    Rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="page-numbers next"]',)), callback="parse", follow= True),)

    def parse(self, response):
        title_in_page = response.xpath('//a[@class="denomination"]/text()').extract()
        for title in title_in_page:
            yield {
                'title': title
            }
        next_page = response.xpath('.//a[@class="page-numbers next"]/@href').extract()
        print("HAHAHAHAH")
        print(next_page)
        if next_page:
            next_href = next_page[0]
            next_page_url = next_href
            request = scrapy.Request(url=next_page_url)
            yield request
