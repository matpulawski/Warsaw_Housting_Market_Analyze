# -*- coding: utf-8 -*-
import scrapy
#from ..items import OtolbnItem

class OtodlbnSpider(scrapy.Spider):
    name = 'otodlbn'
    #allowed_domains = ['https://www.otodom.pl']
    start_urls = ['https://www.otodom.pl/sprzedaz/mieszkanie/warszawa/?nrAdsPerPage=72']


    def parse(self, response):

        #follow the offer detail
        urls = response.css('div.offer-item-details > header > h3 > a::attr(href)').extract()
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse_details)

        #follow pagination link
        next_page_url = response.css('.pager-next a::attr(href)').get()
        if next_page_url:
            print(next_page_url)
            yield scrapy.Request(url = next_page_url, callback = self.parse)


    def parse_details(self, response):

        yield {
            'title':response.css('.css-18igut2::text').extract_first(),
            'district':response.css('.css-12hd9gg::text').extract_first(),
            'price':response.css('.css-1vr19r7::text').extract_first(),
            'bag':response.css('.css-z144hi-Jt ul li').extract(),
            'url':response.request.url
        }