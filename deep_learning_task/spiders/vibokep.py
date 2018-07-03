# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class VibokepSpider(scrapy.Spider):
    name = 'vibokep'
    allowed_domains = ['159.89.201.175']
    start_urls = ['http://159.89.201.175/']

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
