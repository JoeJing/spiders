# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SanguoItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    zi = scrapy.Field()
    pic = scrapy.Field()
    pinyin = scrapy.Field()
    sex = scrapy.Field()
    zhengshi = scrapy.Field()
    shengsi = scrapy.Field()
    jiguan = scrapy.Field()
    content = scrapy.Field()
    cata = scrapy.Field()
