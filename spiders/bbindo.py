# -*- coding: utf-8 -*-
import scrapy


class BbindoSpider(scrapy.Spider):
    name = 'bbindo'
    allowed_domains = ['159.65.130.32']
    start_urls = ['http://159.65.130.32/']


    def parse(self, response):
        next_link = response.xpath('//div[@class="pagination"]/ul/li/a[@class="inactive"]/@href').extract()
        next_link.append('http://159.65.130.32/')
        for link in next_link:
            yield response.follow(link, self.get_all_title)


    def get_all_title(self, response):
        title_in_page = response.xpath('//header[@class="entry-header"]/span/text()').extract()
        for title in title_in_page:
            yield {
                'title': title
            }
       
        
        # title = response.xpath('//header[@class="entry-header"]/span/text()').extract()
        # print(title)
        # print(len(title))
        # yield {
        #         'title': title
        #     }
        # next_page = response.xpath('.//div[@class="pagination"]/ul/li/a[@class="inactive"]/@href').extract()
        # if next_page:
        #     next_href = next_page[0]
        #     next_page_url = next_href
        #     request = scrapy.Request(url=next_page_url)
        #     yield request
        
