# coding:utf8
"""
-------------------------------------------------
    File:   3-2迭代器.py
    Auth:   zsdostar
    Date:   2017/11/19 23:37
    Sys:    Windows 10
-------------------------------------------------
    Desc:   
-------------------------------------------------
"""
__author__ = 'zsdostar'

import requests

# def getWeather(city):
#     r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
#     data = r.json()['data']['forecast'][0]
#     return '%s: %s, %s' % (city, data['low'], data['high'])
# print getWeather(u'北京')
# print getWeather(u'大连')

from collections import Iterable, Iterator


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s' % (city, data['low'], data['high'])

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


if __name__ == '__main__':
    for x in WeatherIterable([u'北京', u'上海', u'广州', u'大连']):
        print x
