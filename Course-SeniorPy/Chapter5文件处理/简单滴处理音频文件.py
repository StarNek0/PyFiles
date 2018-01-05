# coding:utf8
"""
--------------------------------------------------------------------------
    File:   简单滴处理音频文件.py
    Auth:   zsdostar
    Date:   2018/1/3 17:06
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""
__author__ = 'zsdostar'

import array

f = open('demo.wav', 'rb')

info = f.read(44)
import struct
print struct.unpack('h', '\x01\x02')  # example  h:short
print struct.unpack('h', info[22:24])  # 声道数
print struct.unpack('i', info[24:28])  # 采样频率  i:int
print struct.unpack('h', info[34:36])  # 编码宽度

import array
f.seek(0, 2)  # 将文件指针挪到最尾部
f.tell()  # tell报告文件指针位置   在这里其值是这个文件的大小
n = (f.tell() - 44) / 2  # 减去音频文件前44个数据部分的长度，获得数据部分的长度

buf = array.array('h', (0 for _ in range(n)))  # 创建一个大小合适的数组
f.seek(44)
f.readinto(buf)  # 数据读入buf

# example
for i in xrange(n):
    buf[i] /= 8  # 将每个采样减小8倍，这里的效果是将音量减小

f2 = open('demo2.wav0', 'wb')
f2.write(info)
buf.tofile(f2)  # 将数组内容传入文件
f2.close()