#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/14 16:22
# @Author : chenxin
# @Site : 
# @File : quote.py
# @Software: PyCharm
import scrapy
class QuotesSpider(scrapy.Spider):
    name='quotes'
    def start_requests(self):
        urls =[
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self,response):
        page=response.url.split("/")[-2]
        filename="qutoes-%s.html" % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)