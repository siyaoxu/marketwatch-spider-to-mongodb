# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy.selector import Selector
from marketspider.items import MarketspiderItem

class MarketspiderSpider(Spider):
    name = 'marketspider'
    allowed_domains = ['marketwatch.com']
    start_urls = [
            'http://www.marketwatch.com/newsviewer',
            ]
    def parse(self, response):
        # select timesamps and headlines in the 'latest news' tag of newsviewer
        headlines = Selector(response).xpath('//div[@class="nv-text-cont"]/h4')
        timestamps = Selector(response).xpath('//li/@timestamp')
        newsids = Selector(response).xpath('//li/@id')

        for (newsid,timestamp, headline) in zip(newsids,timestamps,headlines):
            item = MarketspiderItem()
            
            item['timestamp'] = timestamp.extract().strip()
            item['newsid'] = newsid.extract().strip()
            if not headline.xpath('a').extract():
                item['title'] = headline.xpath(
                    'text()').extract()[0].strip()
                item['url'] = 'n/a'
                yield item
            else:
                item['title'] = headline.xpath(
                    'a[@class="read-more"]/text()').extract()[0].strip()
                item['url'] = headline.xpath(
                    'a[@class="read-more"]/@href').extract()[0]
                yield item