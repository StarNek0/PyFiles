# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '17-7-2 下午3:10'
# __sys__ = 'CentOS 7'
"""两种方法为元组中的索引命名"""

# 类似于c语言的宏定义方式
NAME = 0
AGE = 1
SEX = 2
EMAIL = 3
# or
NAME, AGE, SEX, EMAIL = xrange(4)

student = ('Jim', 16, 'male', 'a@a.com')
print student

print student[AGE]


print '-----------------------------------------------------------------------'

from collections import namedtuple
Student = namedtuple('student', ['name', 'age', 'sex', 'email'])
s1 = Student('Jim', 16, 'male', '1@1.com')
print s1

s2 = Student(name='Tom', age=13, sex='female', email='')
print s2.age  # 属性访问元组
print isinstance(s1, Student)
print isinstance(s1, tuple)
