from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from livemaster_ru.items import LivemasterRuItem
from scrapy.http import Request


class MySpider(BaseSpider):
    name = "name_and_shop"
    allowed_domains = ["http://www.livemaster.ru/catalogue/kartiny-i-panno"]
    start_urls = ["http://www.livemaster.ru/catalogue/kartiny-i-panno"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        names = hxs.select('//div/div/div[@class="author"]/a').extract()
        for name in names:
            item = LivemasterRuItem()
            item["name"] = name[9:]
            yield item
