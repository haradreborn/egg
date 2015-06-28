from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from livemaster_ru.items import LivemasterRuItem
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class MySpider(BaseSpider):
    name = "name_and_shop"
    allowed_domains = ["livemaster.ru"]
    start_urls = [
        "http://www.livemaster.ru/catalogue/kartiny-i-panno"]

    rules = Rule(SgmlLinkExtractor(allow=()),
        follow=True, callback='parse')

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        names = hxs.select('//div/div/div[@class="author"]/a').extract()
        for name in names:
            item = LivemasterRuItem()
            item["name"] = name
            yield item
