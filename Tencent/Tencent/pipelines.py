# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

from .items import TencentDetailItem, TencentItem


class TencentPipeline(object):
    def open_spider(self, spider):
        self.file = open('tencentList.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, TencentItem):
            dict_data = dict(item)
            str_data = json.dumps(dict_data) + '\n'
            self.file.write(str_data)
        return item

    def close_spider(self, spider):
        self.file.close()

class TencentDetailPipeline(object):
    def open_spider(self, spider):
        self.file = open('tencentDetail.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, TencentDetailItem):
            dict_data = dict(item)
            str_data = json.dumps(dict_data) + '\n'
            self.file.write(str_data)
        return item

    def close_spider(self, spider):
        self.file.close()
