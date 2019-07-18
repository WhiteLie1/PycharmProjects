#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/2 15:02
# @Author : chenxin
# @Site : 
# @File : xml处理.py
# @Software: PyCharm

import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")
root = tree.getroot()
print(root)
print(root.tag)

# 遍历xml文档
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print(i.tag, i.text,i.attrib)

# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)

