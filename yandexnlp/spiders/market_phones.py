# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from bs4 import BeautifulSoup

__author__ = 'Daniel Abramov  github.com/RiskofStorm'


class MarketPhonesSpider(CrawlSpider):
    name = 'market_phones'
    allowed_domains = ['market.yandex.ru']
    start_urls = ["https://market.yandex.ru/catalog--mobilnye-telefony/54726/list?\
    onstock=0&how=opinions&local-offers-first=0"]

    def __init__(self):
        super().__init__()
        # Need more pages to parse? just increase range at self.pages
        self.pages = iter([self.start_urls[0] + "&page={}".format(i) for i in range(1, 20)])
        self.phones_urls = list()

    def parse(self, response):
        data = BeautifulSoup(response.text, 'lxml')

        for phone in data.select("div.n-snippet-cell2__title"):
            self.phones_urls.append(phone.find('a').get('href'))

        next_page_url = next(self.pages, None)
        if next_page_url:
            yield scrapy.Request(next_page_url)
        else:
            with open("ym_phones_urls.txt", 'w+') as out_f:
                out_f.writelines("\n".join(self.phones_urls))
