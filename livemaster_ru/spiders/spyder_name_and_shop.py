from scrapy.spider import CrawlSpider
from scrapy.selector import HtmlXPathSelector
from livemaster_ru.items import LivemasterRuItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
import re


class MySpider(CrawlSpider):
    name = "name_and_shop"
    allowed_domains = ["livemaster.ru"]
    start_urls = ["http://www.livemaster.ru/catalogue/kartiny-i-panno"]

    rules = (Rule(LinkExtractor(allow=r'/kartiny-i-panno\?from=\d+'),
                  callback='parse_names',
                  follow=True),)

    def parse_names(self, response):
        hxs = HtmlXPathSelector(response)
        links = hxs.select('//div/div/div[@class="author"]/a').extract()
        for link in links:
            parser = "^(<a href=\"/).*(\" title=\")(.*)(\|)(.*)(\">).*(</a>)"
            item = LivemasterRuItem()
            data = re.compile(parser).match(link)
            if data:
                item["name"] = data.groups()[2][:-1]
                item["page"] = data.groups()[4][1:]
                yield item
