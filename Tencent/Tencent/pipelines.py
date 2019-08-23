# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class TencentPipeline(object):
    def open_spider(self, spider):
        self.file = open('tencentList.json', 'w')
    def process_item(self, item, spider):

        dict_data = dict(item)
        str_data = json.dumps(dict_data) + '\n'
        self.file.write(str_data)

    def close_spider(self, spider):
        self.file.close()