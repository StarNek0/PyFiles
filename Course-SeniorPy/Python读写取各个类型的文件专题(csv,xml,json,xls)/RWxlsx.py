# coding:utf8
"""
--------------------------------------------------------------------------
    File:   RWxlsx.py
    Auth:   zsdostar
    Date:   2018/1/4 23:04
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   关于Python操作Excel的演示
--------------------------------------------------------------------------
"""
__author__ = 'zsdostar'

import xlrd  # xls read 读Excel
import xlwt  # xls write 写Excel

work_book = xlrd.open_workbook('demo.xlsx')  # 读取Excel

work_book.sheets()  # 返回整个表

sheet = work_book.sheet_by_index(0)  # 或返回第[0]个sheet页

print sheet.nrows  # 几行
print sheet.ncols  #几列

cell = sheet.cell(0, 0)  # 按坐标读取，这就是sheet1里面A1格的对象
# cell有以下参数： cell.ctype cell.dump cell.value cell.xf_index
print cell


print sheet.row(1)  # 读取一行
print sheet.row_values(rowx=2, start_colx=1)  # 第[2]行，从这行的第[1]个开始取数据

# sheet.put_cell(0, 0, xlrd.XL_CELL_NUMBER, t, None)  (行，列，格式，值, style)


# --------------------------------------------------------------------------------------


work_book = xlwt.Workbook()

work_book_sheet = work_book.add_sheet('sheet1')
work_book_sheet.write()  # (行，列，值，style)
work_book.save('output.xlsx')