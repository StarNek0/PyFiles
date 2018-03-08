# coding:utf8
"""
--------------------------------------------------------------------------
    File:   sort.py
    Auth:   zsdostar
    Date:   2018/3/8 13:57
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""
import time

def solve(dates):
    for date in dates:
        st = time.mktime(time.strptime(date[1]['date'], "%Y-%m-%d"))
        date[1]['date_float'] = float(st)

    dates = sorted(dates,key=lambda k:k[1]['date_float'],reverse=True)

    for date in dates:
        date[1].pop('date_float')
    return dates


if __name__ == '__main__':
    dates = [(2, {"date": "2015-3-2"}, "tom"),
             (1, {"date": "2015-3-1"}, "jack"),
             (3, {"date": "2015-3-3"}, "tom"), ]
    print dates
    print solve(dates)