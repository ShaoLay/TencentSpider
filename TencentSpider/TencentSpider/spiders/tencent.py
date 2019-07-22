# -*- coding: utf-8 -*-
import scrapy

from TencentSpider.items import TencentspiderItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/search.html?index=2']

    def parse(self, response):

        for each in response.xpath('//div[@class="recruit-list"]'):
            item = TencentspiderItem()
            titile = each.xpath('.//h4[@class="recruit-title"]').extract()[0]
            bu_men = each.xpath('.//a[@class="recruit-list-link"]//span[1]').extract()[0]
            work_addrress = each.xpath('.//a[@class="recruit-list-link"]//span[2]').extract()[0]
            work_type = each.xpath('.//a[@class="recruit-list-link"]//span[3]').extract()[0]
            pubdate = each.xpath('.//p[@class="recruit-tips"]//span[last()]').extract()[0]

            item['title'] = titile
            item['bu_men'] = bu_men
            item['work_address'] = work_addrress
            item['work_type'] = work_type
            item['pubdate'] = pubdate

            yield item



