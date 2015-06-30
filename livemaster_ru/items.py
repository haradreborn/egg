# -*- coding: utf-8 -*-
import scrapy


class LivemasterRuItem(scrapy.Item):
    name = scrapy.Field()
    page = scrapy.Field()
