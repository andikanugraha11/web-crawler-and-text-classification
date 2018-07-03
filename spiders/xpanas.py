# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class XpanasSpider(scrapy.Spider):
    name = 'xpanas'
    allowed_domains = ['192.243.98.23']
    start_urls = [
        'http://192.243.98.23/category/asian-porn/',
        'http://192.243.98.23/category/bokep-indo/',
        'http://192.243.98.23/category/bokep-jepang/',
        'http://192.243.98.23/category/bokep-barat/'
        
        ]

    # Rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="pagination"]/ul/li/a',)), callback="parse", follow= True),)

    def parse(self, response):

        last_page = response.xpath('//div[@class="pagination"]/ul/li/a/@href').extract()
        print(len(last_page))
        # print(link_next)
        all_link = []
        if len(last_page) > 0:
            last_page_link = last_page[-1]
            last_page_identifier = last_page_link.find('page')
            link_next = last_page_link[last_page_identifier+5:-1]
            for x in range(int(link_next)):
                page = x+1
                all_link.append(response.url+'page/'+str(page))
        else:
            all_link.append(response.url)
        print(all_link)
        
        for link in all_link:
            yield response.follow(link, self.get_all_title)

    def get_all_title(self, response):
        title_in_page = response.xpath('//header[@class="entry-header"]/span/text()').extract()
        for title in title_in_page:
            yield {
                'title': title
            }
       