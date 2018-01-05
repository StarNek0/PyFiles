# coding:utf8
"""
--------------------------------------------------------------------------
    File:   5-6临时文件.py
    Auth:   zsdostar
    Date:   2018/1/4 21:12
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   某项目中，我们从传感器采集数据，每收集到 1G 数据后，做数据分析，
            最终只保存分析结果。这样很大的临时数据如果常驻内存，
            将消耗大量内存资源，
            我们可以使用临时文件存储这些临时数据（外部存储）。
            临时文件不用命名，且关闭后会自动被删除。
            使用TemporaryFile, NamedTemporaryFile
--------------------------------------------------------------------------
"""
__author__ = 'zsdostar'

from tempfile import TemporaryFile, NamedTemporaryFile

f = TemporaryFile()
f.write('abcdef' * 10000)

# 当收集的数据量足够时
# 文件指针扔到开头
f.seek(0)

f.read(100)  # 读入一部分


# NamedTemporaryFile生成的临时文件可在文件系统中找到
# 在参数里设置delete=False即可在让临时文件不被自动删除
ntf = NamedTemporaryFile()
print ntf.name  # 就是它的路径