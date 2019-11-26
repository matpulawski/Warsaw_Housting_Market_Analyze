# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OtolbnItem(scrapy.Item):
    # define the fields for your item here like:
    # define the fields for your item here like:
    title = scrapy.Field()
    district = scrapy.Field()
    price = scrapy.Field()
    area = scrapy.Field()
    room = scrapy.Field()
    market = scrapy.Field()
    type_of_building = scrapy.Field()
    floor = scrapy.Field()
    number_of_floor = scrapy.Field()
    house_material = scrapy.Field()
    window = scrapy.Field()
    heating = scrapy.Field()
    rent = scrapy.Field()
    type_of_prop = scrapy.Field()

