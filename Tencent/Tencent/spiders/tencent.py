# -*- coding: utf-8 -*-
import json
import re

import scrapy

from Tencent.items import TencentItem, TencentDetailItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    end_url = '&pageSize=10'
    begin_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex='
    url_list = []
    for page in range(1, 507):
        url = begin_url + str(page) + end_url
        print('我是url:', url)
        url_list.append(url)

    start_urls = url_list


    def parse(self, response):
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

            post_id = item['work_link']
            content = re.findall(r'\d+', post_id)

            detail_link = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?&postId=' + content[0]

            yield item

            yield scrapy.Request(detail_link, callback=self.details_parse)

    def details_parse(self, response):
        site = json.loads(response.body_as_unicode())
        site = site['Data']
        item = TencentDetailItem()
        item['work_duty'] = site['Responsibility']
        item['work_requir'] = site['Requirement']
        yield item
