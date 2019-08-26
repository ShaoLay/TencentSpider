# -*- coding: utf-8 -*-
import json

import scrapy

from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    page = 1
    end_url = '&pageSize=10'
    base_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex='
    start_urls = [base_url + str(page) + end_url]

    def parse(self, response):
        print('$' * 100)
        print('结果是:', response.url)

        if self.page > 499:
            return

        sites = json.loads(response.body_as_unicode())
        sites = sites['Data']
        sites = sites['Posts']
        for site in sites:
            item = TencentItem()

            item['work_name'] = site['RecruitPostName']
            item['work_type'] = site['CategoryName']
            item['work_country'] = site['CountryName']
            item['work_place'] = site['LocationName']
            item['work_time'] = site['LastUpdateTime']
            item['work_link'] = site['PostURL']

            yield item

        self.page += 1
        url = self.base_url + str(self.page) + self.end_url
        yield scrapy.Request(url, callback=self.parse)
