#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/4 20:40
# @Author : chenxin
# @Site : 
# @File : xml修改.py
# @Software: PyCharm

import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")
root = tree.getroot()
print(root)
print(root.tag)

# 修改
for node in root.iter('year'):
    new_year = int(node.text)+1
    node.text = str(new_year)
    node.set('updated_by','alex')

tree.write('xmltest.xml')

# 删除  node
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank >50:
        root.remove(country)
tree.write('output.xml')