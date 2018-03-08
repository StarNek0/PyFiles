# coding:utf8
"""
--------------------------------------------------------------------------
    File:   exam_txt_to_dict.py
    Auth:   zsdostar
    Date:   2018/3/8 15:21
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""
import re
# with open('file','r') as f:
#     doc = f.read()
doc = "2687694\t18070300\n2687694\t18070300\n2687694\t18070500\n2687694\t18070500\n2687697\t15050000\n2687697\t15050000\n2687697\t15050500\n2687697\t15050500\n"

print doc


def solve(doc):
    doc = re.findall('(\d+)\t(\d+)\n',doc)
    # print doc
    keys = []
    values = []
    for d in doc:
        keys.append(d[0])
        values.append(d[1])
    # print list(set(keys)),values

    for key in list(set(keys)):
        print key+':',
        for i in doc:
            if i[0]==key:
                print i[1]+','+ str(values.count(i[1]))+';',
        print

if __name__ == '__main__':
    solve(doc)