# -*- coding: utf-8 -*-
import scrapy


class AoraSpider(scrapy.Spider):
    name = 'aora'
    allowed_domains = ['128.199.102.111']
    start_urls = ['http://128.199.102.111/']

    def parse(self, response):
        next_link = response.xpath('//div[@class="pagination"]/ul/li/a[@class="inactive"]/@href').extract()
        next_link.append('http://128.199.102.111/')
        for link in next_link:
            yield response.follow(link, self.get_all_title)


    def get_all_title(self, response):
        title_in_page = response.xpath('//header[@class="entry-header"]/span/text()').extract()
        for title in title_in_page:
            yield {
                'title': title
            }
