#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/14 9:23
# @Author : chenxin
# @Site : 
# @File : makeup.py
# @Software: PyCharm
import scrapy
import json


class MakeupSpider(scrapy.Spider):
    name = 'makeup'
    allowed_domains = ['www.search.jumei.com']

    def start_requests(self):
        searchname = "保湿"
        url = 'http://search.jumei.com/?filter=0-11-{0}&search={1}'
        for i in range(1, 20):
            yield scrapy.Request(url=url.format(i, searchname),
                                 callback=self.parse)

    def parse(self, response):
        for item in response.css('li.hai.item'):
            makeitem = {}
            name = item.css('div.s_l_name a::text').get()
            image = item.css('div.s_l_pic img::attr(src)').get()
            price = item.css('div.s_l_view_bg span::text').get()
            interurl = item.css('div.s_l_name a::attr(href)').get()
            nameret = name.strip()
            nameret = nameret.replace('\"', '')
            nameret = nameret.replace('\n', '')
            makeitem["name"] = nameret
            makeitem["price"] = float(price)
            makeitem["thumbnail"] = image
            makeitem["detailImage"] = [image]
            interurl = response.urljoin(interurl)
            yield scrapy.Request(url=interurl, meta={'item': makeitem},
                                 callback=self.parse2, dont_filter=True)

    def parse2(self, response):
        self.log('hello')
        makeupitem = response.meta['item']
        for it in response.css('div.content_text tr'):
            name = it.css('b::text').get()
            name = name.strip()
            name = name.replace(' ', '')
            content = it.css('span::text').get()
            content = content.strip()
            content = content.replace(' ', '')
            if name == '商品型号：':
                makeupitem["sku"] = content
            if name == '功效：':
                tmp = content.split(',')
                makeupitem["tag"] = tmp
            if name == '原产国家：':
                makeupitem["originCountry"] = content
            if name == '品牌：':
                makeupitem["brand"] = content
            if name == '分类：':
                makeupitem["category"] = content
        f = open("test.txt.json", 'a+', encoding='utf-8')
        ret = json.dumps(makeupitem)
        ret = ret + ',\n'
        f.write(ret)
        f.close()




