# coding:utf8
import exceptions
# __author__ = 'zsdostar'
# __date__ = '2017/4/27 13:21'
__doc__ = '''
***一些內建异常***
Exception           所有异常的基类
AttributeError      特性引用或赋值失败
IOError             打开不存在的文件
IndexError          不存在的索引
KeyError            映射中不存在的键
NameError           找不到名字(变量)
SyntaxError         代码是错误形式
TypeError           函数应用于错误类型的对象
ValueError          正确的对象但是值不合适
ZeroDivisionError   除零错误
***自定义异常类***
class SomeException(Exception):
    pass
'''
# try:
#     print 1/0
# except ZeroDivisionError as zero:
#     print 'zero error!'
# else:
#     print 1
#

# import urllib2
# for i in dir(urllib2):
#     print i

# import exceptions
# for i in dir(exceptions):
#     print i
# print exceptions.__name__

# * x = int(raw_input('Enter the first number:'))
# * y = int(raw_input('Enter the second number:'))
# x = input('Enter the first number:')
# y = input('Enter the second number:')
# try:
#     print x/y
# except (ZeroDivisionError, TypeError) as e:
#     # print u'第二个数不应该是0'
#     print e

# x = input('Enter the first number:')
# y = input('Enter the second number:')
# try:
#     print x/y
# except (ZeroDivisionError, TypeError) as e:
#     print e

# class Calc(object):
#     muffled = False
#
#     def calc(self, expr):
#         try:
#             return eval(expr)
#         except (ZeroDivisionError, TypeError):
#             if self.muffled:
#                 print 'Division by zero is illegal!'
#             else:
#                 raise
#
# calc1 = Calc()
# calc1.muffled = True
# print calc1.calc('10/0')

'''8.8 异常时循环，直到正常读取时退出'''
# while True:
#     try:
#         x = input('First num:')
#         y = input('Second num:')
#         value = x/y
#     except:
#         print 'Invalid input. Please try again!'
#     else:
#         break

'''9 魔法方法、属性和迭代器'''


# class TesCase(object):  # 不要创建包含字符test的类
#     auto = 1
#
#     def __init__(self):
#         self.auto += 1
#
# test = TesCase()
# print test.auto


# class Bird(object):
#     def __init__(self):
#         self.hungry = True
#
#     def eat(self):
#         if self.hungry:
#             print 'eating..."tasty food!"'
#             self.hungry = False
#         else:
#             print 'No,thanks.'
#
#
# class SongBird(Bird):
#     def __init__(self):
#         # 第一种
#         # Bird.__init__(self)
#         # 第二种
#         # super(SongBird, self).__init__()
#         self.sound = 'Squawl!'
#
#     def sing(self):
#         print self.sound
#
#
# sb = SongBird()
# sb.sing()
# sb.eat()

'''9.5'''

#
# class Rectangle(object):
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#
#     def set_size(self, size):
#         self.width, self.height = size
#
#     def get_size(self):
#         return self.width, self.height
#
#     size = property(get_size, set_size)
# r = Rectangle()
# r.width = 10
# r.height = 5
# print r.size
# r.size = 150, 100

# 装饰器
# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

# 函数调用
# class Student(object):
#
#     def get_score(self):
#         return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#     score = property(get_score, set_score)

# s = Student
# s.score = 60
# print s.score
# s.score = 9999

# 特殊方法
# class Rectangle(object):
#     def __init__(self):
#         self.width = None
#         self.height = None
#     def __setattr__(self, key, value):
#         if key == 'size':
#             self.width, self.height = value
#         else:
#             self.__dict__[key] = value
#     def __getattr__(self, item):
#         if item == 'size':
#             return self.width, self.height
#         else:
#             raise AttributeError
'''9.6迭代器'''
# class Fibs(object):
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#
#     def next(self):
#         self.a, self.b = self.b, self.a+self.b
#         return self.a
#
#     def __iter__(self):
#         return self
#
# fibs = Fibs()
# for f in fibs:
#     if f > 1000:
#         print f
#         break

#
# class TestIterator(object):
#     value = 0
#
#     def next(self):
#         self.value += 1
#         if self.value > 10:
#             raise StopIteration
#         return self.value
#
#     def __iter__(self):
#         return self
#
# ti = TestIterator()
# print list(ti)

'''9.7生成器'''

#
# def flatten(nested):
#     try:
#         try: nested + ''
#         except TypeError: pass
#         else: raise TypeError
#
#         for sublist in nested:
#             for element in flatten(sublist):
#                 yield element
#     except TypeError:
#         yield nested
#
# # nested = [[1, 2], [3, 4], [5]]
# print list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8]))


def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new

r = repeater(42)
print r.next()
print r.send('Hello')
'''End'''
'''The next problem is eight queens'''
