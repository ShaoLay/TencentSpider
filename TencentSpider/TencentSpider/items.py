# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentspiderItem(scrapy.Item):
    # define the fields for your item here like:

    title = scrapy.Field()
    bu_men = scrapy.Field()
    work_address = scrapy.Field()
    work_type = scrapy.Field()
    pubdate = scrapy.Field()
