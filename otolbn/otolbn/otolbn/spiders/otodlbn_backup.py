# -*- coding: utf-8 -*-
'''
import scrapy
from ..items import OtolbnItem

class OtodlbnSpider(scrapy.Spider):
    name = 'otodlbn'
    allowed_domains = ['https://www.otodom.pl']
    start_urls = ['https://www.otodom.pl/sprzedaz/mieszkanie/warszawa/?nrAdsPerPage=72']

    def start_requests(self):

        domain = "https://www.otodom.pl/sprzedaz/mieszkanie/warszawa/?nrAdsPerPage=72&page="

        for page_number in range(1, 279):

            www_site = domain + str(page_number)
            yield scrapy.Request(url=www_site, callback=self.parse)

    def parse(self, response):
       # urls = response.css("div.offer-item-details.header.h3 a::attr(href)").extract()
       # for url in urls:
       #     yield scrapy.Request(url=url, callback=self.parse_one_page)
        items = OtolbnItem()
        all_div = response.css("article")

        for div in all_div:

            title = div.css('.offer-item-title::text').extract()
            district = div.css('p.text-nowrap::text').extract()
            rooms = div.css('.offer-item-rooms::text').extract()
            area = div.css('.offer-item-area::text').extract()
            price = div.css('.offer-item-price::text').extract()

            items['title'] = title
            items['district'] = district
            items['room'] = rooms
            items['area'] = area
            items['price'] = price

            yield items


        #next_page = 'https://www.otodom.pl/sprzedaz/mieszkanie/lublin/?nrAdsPerPage=72&page=' + str(OtodlbnSpider.page_number)

        #while OtodlbnSpider.page_number < 40:
        #    OtodlbnSpider.page_number += 1
        #    yield response.follow(next_page, callback = self.parse)


'''
'''
     def parse_one_page(self, response):
        items = OtolbnItem()

        title = response.css('.css-18igut2::text').extract()
        district = response.css('.css-12hd9gg::text').extract()
        price = response.css('.css-1vr19r7::text').extract()
        area = response.css('.css-1kgyoyz-Xt li:nth-child(1) strong::text').extract()
        room = response.css('li:nth-child(2) strong::text').extract()
        market = response.css('li:nth-child(3) strong::text').extract()
        type_of_building = response.css('li:nth-child(4) strong::text').extract()
        floor = response.css('li:nth-child(5) strong::text').extract()
        number_of_floor= response.css('li:nth-child(6) strong::text').extract()
        house_material = response.css('li:nth-child(7) strong::text').extract()
        window = response.css('li:nth-child(8) strong::text').extract()
        heating = response.css('li:nth-child(9) strong::text').extract()
        rent = response.css('li:nth-child(11) strong::text').extract()
        type_of_prop = response.css('li:nth-child(12) strong::text').extract()


        items['title'] = title
        items['district'] = district
        items['price'] = price
        items['area'] = area
        items['room'] = room
        items['market'] = market
        items['type_of_building'] = type_of_building
        items['floor'] = floor
        items['number_of_floor'] = number_of_floor
        items['house_material'] = house_material
        items['window'] = window
        items['heating'] = heating
        items['rent'] = rent
        items['type_of_prop'] = type_of_prop

        yield items
'''