# coding:utf8
"""
--------------------------------------------------------------------------
    File:   load_dump_json.py
    Auth:   zsdostar
    Date:   2018/1/4 22:02
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""
__author__ = 'zsdostar'

import requests
import json

l = [1, 2, 'abc', {'name': 'Bob', 'age': 13}]
print json.dumps(l)
# [1, 2, "abc", {"age": 13, "name": "Bob"}]

d = {'b': None, 'a': 5, 'c': 'abc'}
print json.dumps(d)
# {"a": 5, "c": "abc", "b": null}

json.dumps(l, separators=[',', ':'])  # 正常是', '和': '。   这样改，就可以消去空格存储
json.dumps(d, sort_keys=True)  # 改成key貌似就可以按key字典序排序了

# dumps把dict、list啥的生成一串json风格字符串

# loads正好相反，把json风格字符串数据变成dict之类的
s = json.loads('''{
"employees": [
{ "firstName":"Bill" , "lastName":"Gates" },
{ "firstName":"George" , "lastName":"Bush" },
{ "firstName":"Thomas" , "lastName":"Carter" }
]
}''')

# dump把数据写进文件
with open('demo.json', 'wb') as f:
    json.dump(s, f)
