# coding:utf8
"""
--------------------------------------------------------------------------
    File:   为的demo.xlsx统计总成绩.py
    Auth:   zsdostar
    Date:   2018/1/4 23:23
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""
import xlrd, xlwt

rbook = xlrd.open_workbook('demo.xlsx')
rsheet = rbook.sheet_by_index(0)
rsheet.put_cell(0, rsheet.ncols, xlrd.XL_CELL_TEXT, u'总分', None)  # 写入'总分'两个字

# 根据三科成绩计算总成绩
for row in xrange(1, rsheet.nrows):
    t = sum(rsheet.row_values(row, 1))
    rsheet.put_cell(0, rsheet.ncols, xlrd.XL_CELL_NUMBER, t, None)


wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)

# 把读到的和算到的全盘copy写入
for r in range(rsheet.nrows):
    for c in range(4):
        wsheet.write(r, c, rsheet.cell_value(r, c))

wbook.save('output.xlsx')

# IndexError: list index out of range
# 发现列范围有点不对劲，改为4
# 虽然没抛异常，但是文件损坏。。。。