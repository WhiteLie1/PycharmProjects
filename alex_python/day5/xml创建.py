#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/5 16:09
# @Author : chenxin
# @Site : 
# @File : xml创建.py
# @Software: PyCharm

import xml.etree.ElementTree as ET

new_xml = ET.Element("personinfolist")
personinfo = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "yes"})
name= ET.SubElement(personinfo, "name",attrib={'checked':'no'})
name.text = 'alex'

age = ET.SubElement(personinfo, "age", attrib={"checked": "no"})
sex = ET.SubElement(personinfo, "sex")
age.text = '33'
personinfo2 = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "no"})
name = ET.SubElement(personinfo2, "name")
name.text = 'oldboy'
age = ET.SubElement(personinfo2,'age')
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.txt.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式

