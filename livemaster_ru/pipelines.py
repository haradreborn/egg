# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem


class LivemasterRuPipeline(object):

    def __init__(self):
        self.pages_seen = set()

    def process_item(self, item, spider):
        if item['page'] in self.pages_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.pages_seen.add(item['page'])
            return item
