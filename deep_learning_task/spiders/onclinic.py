# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from termcolor import colored

class OnclinicSpider(scrapy.Spider):
    name = 'onclinic'
    allowed_domains = ['onclinic.co.id']
    start_urls = [
        'https://onclinic.co.id/artikel/',
        'https://onclinic.co.id/category/info-kesehatan/']

    Rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="next page-numbers"]',)), callback="parse", follow= True),)


    def parse(self, response):
        article_link = response.xpath('//h2[@class="hentry__title"]/a/@href').extract()
        print(colored(response.url,'red'))
        print(colored(article_link,'green'))
        
        for link in article_link:
            yield response.follow(link, self.get_all_article)

        next_page = response.xpath('.//a[@class="next page-numbers"]/@href').extract()
        if next_page:
            next_href = next_page[0]
            next_page_url = next_href
            request = scrapy.Request(url=next_page_url)
            yield request

    def get_all_article(self, response):
        contents = response.xpath('//div[@class="hentry__content"]/p/text()').extract()
        content =  " ".join(str(x) for x in contents)
        yield {
            'content': content
        }
       