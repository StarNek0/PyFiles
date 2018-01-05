# coding:utf8
"""
--------------------------------------------------------------------------
    File:   rwxml.py
    Auth:   zsdostar
    Date:   2018/1/5 10:01
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""


from xml.etree.ElementTree import parse

with open('demo.xml') as f:
    et = parse(f)
    root =  et.getroot()
    print root.tag  # 标签
    print root.attrib  #字典
    print root.text.strip()

    for child in root:
        print child.get('name')

    print root.iterfind('XPStyle')
    print root.findall('KeyWord')
    print list(root.iter())