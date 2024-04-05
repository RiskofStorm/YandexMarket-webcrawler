# -*- coding: utf-8 -*-

from scrapy.item import Item, Field
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class YandexnlpPipeline(object):

    def __init__(self):
        super().__init__()
        self.file = None

    def open_spider(self, spider):
        self.file = csv.writer(open('reviews_yandexmarket.csv', 'w+'))

    def close_spder(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.writerow((item['marks'], item['reviews']))
        return item
