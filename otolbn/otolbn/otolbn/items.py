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
    bag = scrapy.Field()
    url = scrapy.Field()

