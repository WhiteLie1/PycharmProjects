#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/14 16:26
# @Author : chenxin
# @Site : 
# @File : taobao.py
# @Software: PyCharm
import scrapy


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['www.list.tmall.com']

    def start_requests(self):
        url = "https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.5d56adbfzgZdo6&s={0}&q=%B9%D9%B7%BD%D6%B1%CA%DB&sort=s&style=g&vmarket=29890&active=2&theme=275&smAreaId=330100&type=pc#J_Filter"
        self.log('hello')
        self.log(url.format(0))
        yield scrapy.Request(url=url.format(0), callback=self.parse)

    def parse(self, response):
        self.log('parse')
        for item in response.css('div.product'):
            image = item.css('div.productImg-wrap img::attr(src)').get()
            price = item.css('p.productPrice em::text').get()
            name = item.css('p.productTitle a::text').get()
            url = item.css('p.productTitle a::attr(href)').get()
            f = open('test2.txt', 'a+')
            f.write(image)
            f.write(price)
            f.write(name)
            f.close()
            # yield scrapy.Request(url=url,callback=self.parse2)

    # def parse2(self,response):
    #     ret=[]
    #     for item in response.css('div.attributes ul li::text'):
    #         ret.append(item)
    #     f=open('test2.txt','a+')
    #     for i in ret:
    #         f.write(i)
    #     f.close()


