# -*- coding: utf-8 -*-

import scrapy


class TencentSpider(scrapy.Spider):
    name = 'tencent2'
    allowed_domains = ['tencent.com']
    start_urls = 'https://careers.tencent.com/search.html'

    def parse(self, response):
        filename = 'tencent2.html'
        open(filename, 'wb').write(response.body)
