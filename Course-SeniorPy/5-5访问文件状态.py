# coding:utf8
"""
--------------------------------------------------------------------------
    File:   5-5访问文件状态.py
    Auth:   zsdostar
    Date:   2018/1/4 20:46
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   最好放到linux上跑
--------------------------------------------------------------------------
"""
__author__ = 'zsdostar'


import os

print os.stat('__init__.py')
print bin(os.stat('__init__.py').st_mode)  # 解码为二进制
# 仍然不是想要的数据

import stat
print stat.S_ISDIR(os.stat('__init__.py').st_mode)  # 是否是目录
print stat.S_ISREG(os.stat('__init__.py').st_mode)  # 是否是文件

print os.stat('__init__.py').st_mode & stat.S_IRUSR  # 查看权限
print os.stat('__init__.py').st_mode & stat.S_IXUSR  # 同上


print os.stat('__init__.py').st_atime  # 1502716516.66 最后访问时间的秒数 这不是最终想要的数据
import time
print time.localtime(os.stat('__init__.py').st_atime)  # 从以上时间中获得人类能认出的数据

print os.stat('__init__.py').st_size  # 文件大小


# 第二种方法，os.path的方法
os.path.isdir('')
os.path.islink('')
os.path.isfile('')

os.path.getatime('')