# -*- coding: utf-8 -*-
#上一行 目的是告诉Python解释器，用UTF-8编码读取源代码。然后用Notepad++ 另存为... 并选择UTF-8格式保存。
#print (45678+0x12fd2)
#print 'Learn Python in imooc'
#print 100 < 99
#print 0xff == 255
#-------------------------------------------------------------------------------------
#print 'The quick brown fox','jumps over','The lazy dog'
#-------------------------------------------------------------------------------------
#print 300
#print 100 + 200
#-------------------------------------------------------------------------------------
#print '100 + 200 =',100 + 200
#print 'hello, python'
#print 'hello,','python'#When meet "," may print an extra space
#-------------------------------------------------------------------------------------
#x1 = 1
#d = 3
#n = 100
#x100 = x1 + (n-1)*d
#s = n*x1 + n*(n-1)*d/2
#print s
#-------------------------------------------------------------------------------------
#s = 'Python was started in 1989 by "Guido".\nPython is free and easy to learn.'
#print s
#-------------------------------------------------------------------------------------
#print r'''"To be, or not to be": that is the question.
#Whether it's nobler in the mind to suffer.'''
#-------------------------------------------------------------------------------------
#print u'''静夜思
#床前明月光，
#疑是地上霜。
#举头望明月，
#低头思故乡。'''
#-------------------------------------------------------------------------------------
#print 2.5 + 10 / 4
#-------------------------------------------------------------------------------------
#a = 'python'
#print 'hello,', a or 'world'
#b = ''
#print 'hello,', b or 'world'
#-------------------------------------------------------------------------------------
#L = ['Adam', 'Lisa', 'Bart']
#L.insert(2,"Paul")
#print L

#L = ['Adam', 'Lisa', 'Paul', 'Bart']
#L.pop(2)
#L.pop(2)
#print L

'''sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x%2==0:
        continue
    sum=sum+x
print sum'''

'''import urllib2
response = urllib2.urlopen("http://www.baidu.com")
print response.getcode()
cont = response.read()'''

'''
import urllib2
request = urllib2.Request("http://www.baidu.com")
#request.add_data('a','1')
request.add_header('User-Agent','Mozilla/5.0')
response = urllib2.urlopen("http://www.baidu.com")
'''

'''
#cookie
import urllib2,cookielib
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response = urllib2.urlopen("http://www.baidu.com")
'''
'''
#coding:utf-8
import urllib2
url = "http://www.baidu.com"
print '第一种方法'.decode("utf-8")
response1 = urllib2.urlopen(url)

print response1.getcode()
print len(response1.read())
'''

'''
#dict Operathing
#dict key:value
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}
print len(d) #输出d的长度
'''
#dict's Special Point: http://www.imooc.com/code/3501
'''
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print 'Adam: ',d['Adam']
print 'Lisa: ',d['Lisa']
print 'Bart: ',d['Bart']
'''

'''
d = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart',
}
d[72]='Paul'
print d
'''
'''
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in d:
    print key, ':', d[key]
'''
'''
months = set(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
x1 = 'Feb'
x2 = 'Sun'

if x1 in months:
    print 'x1: ok'
else:
    print 'x1: error'

if x2 in months:
    print 'x2: ok'
else:
    print 'x2: error'
'''
#*********************!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for name in s:
    print name[0], ':', name[1]
'''

'''
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for adn in L:
    if adn in s:
        s.remove(adn)
    else:
        s.add(adn)
print s
'''

'''
L = []
i=1
while i <= 100:
    L.append(i * i)
    i = i + 1
print sum(L)
'''
'''
def square_of_sum(L):
    sumas=0
    for i in L:#此处的i并非索引，而是数据
        sumas = sumas + i*i
    return sumas
print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])
'''
'''
import math

def quadratic_equation(a, b, c):
    outnum1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)#此处2*a必须加括号
    outnum2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
    return outnum1,outnum2
print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)
#以下为较为规范的代码
'''
'''
import math
def quadratic_equation(a, b, c):
    t = math.sqrt(b * b - 4 * a * c)
    return (-b + t) / (2 * a),( -b - t )/ (2 * a)
print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)
'''

'''Task
汉诺塔的移动也可以看做是递归函数。
我们对柱子编号为a, b, c，将所有圆盘从a移到c可以描述为：
如果a只有一个圆盘，可以直接移动到c；
如果a有N个圆盘，可以看成a有1个圆盘（底盘） + (N-1)个圆盘，首先需要把 (N-1) 个圆盘移动到 b，然后，将 a的最后一个圆盘移动到c，再将b的(N-1)个圆盘移动到c。
请编写一个函数，给定输入 n, a, b, c，打印出移动的步骤：
move(n, a, b, c)
例如，输入 move(2, 'A', 'B', 'C')，打印出：
A --> B
A --> C
B --> C
'''
'''
def move(n, a, b, c):
    if n!=1:
        move(n-1,a,c,b)#以c为辅助点把a底座移动到b
        move(1,a,b,c)#极点时以b为辅助点把a移动到c
        move(n-1,b,a,c)#以a为辅助点把b其余的移动到c
    else:
        print a,'-->',c

move(4, 'A', 'B', 'C')
'''
'''Task
请定义一个 greet() 函数，它包含一个默认参数，如果没有传入，打印 'Hello, world.'，如果传入，打印 'Hello, xxx.'.
'''
'''
def greet(a=1):
    if a==1:
        print 'Hello,world.'
    else:
        print 'Hello,',a
greet()
greet('Bart')
'''
'''
def average(*args):
    sum = 0.0
    for i in args:
        sum = sum + i
    if len(args)!=0:#此处为应注意点
        sum = sum / len(args)
    else:
        sum=0.0
    return sum
print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)
'''
# create a array L[1,2,3,...,100]

'''
L = range(1,101)

print L[:10]
print L[2::3]
print L[4:50:5]
'''

'''L = range(1, 101)
print L[-10:]
print L[-11::5]
'''

'''
L = ['Adam', 'Lisa', 'Bart', 'Paul']
print L[-2:]
print L[-4:-2]  # 此处右边为不包括边界
print L[-3:-1]  # 同上
print L[-4:-1:2]
'''

'''
任务
利用倒序切片对 1 - 100 的数列取出：
* 最后10个数；
* 最后10个5的倍数。

L = range(1, 101)
print L[-10:]
print L[-46::5]
'''
'''
def firstCharUpper(s):
    return s[:1].upper()+s[1:]  # 此处用+可以输出连接好的字符串否则“，”就是一个tuple,并且“，”会形成一个空格

print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')
'''
'''for i in range(1,101):
    if i%7 == 0:
        print i
'''

'''
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for t in enumerate(L):
    index = t[0]
    name = t[1]
    print index, '-', name
# 等价于以下代码片
for index, name in enumerate(L):  # --------------------------重要
    print index, '-', name
'''
'''
L = ['Adam', 'Lisa', 'Bart', 'Paul']

for index, name in zip(range(1, len(L)+1), L):
    print index, '-', name
print range(1, len(L)+1), L
print zip(range(1, len(L)+1), L)
'''
# 9.3
'''
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for i in d:
    sum = sum + d[i]
print sum / len(d)
'''
# 等同于以下代码片
'''
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for i in d.values():  # -------------------------------------重要
    sum = sum + i
print sum/len(d)
'''

'''
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for k, v in d.items():  # -----------------------------------重要
    sum = sum + v
    print k,':',v
print 'average', ':', sum / len(d)
'''
# print [i*(i+1) for i in range(1,100,2)]
'''d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.iteritems()]
print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
'''

# print [x*x for x in range(1, 11)]  # output:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# print [x*x for x in range(1, 11) if x*x % 2 == 0]  # output:[4, 16, 36, 64, 100]

'''
def toUppers(L):
    return [i.upper() for i in L if isinstance(i,str)]
print toUppers(['Hello', 'world', 101])

# output ['HELLO', 'WORLD']
# 1. isinstance(x, str) 可以判断变量 x 是否是字符串；
# 2. 字符串的 upper() 方法可以返回大写的字母。
'''

# print [m + n for m in 'ABC' for n in '123']  # out:['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

# print [a+b for a in '12345' for b in '12345']  # out:['11', '12', '13', '14', '15', '21', '22', '23', '24', '25', '31', '32', '33', '34', '35', '41', '42', '43', '44', '45', '51', '52', '53', '54', '55']

# 利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。
'''
print [100*int(a)+10*int(b)+int(c) for a in '123456789' for b in '0123456789' for c in '0123456789' if a==c]  # 我的代码
print [100 * n1 + 10 * n2 + n3 for n1 in range(1, 10) for n2 in range(10) for n3 in range(10) if n1==n3]  # 答案
print [x for x in range(100,1000) if x/100 ==x%10]  # 取巧代码
'''

'''import math

def add(x, y, f):
    return f(x) + f(y)

def sqrt(num):
    i=0.0
    while(i<(num/2.0)):
        if(i*i==num):
            return i
        i=i+1.0
print add(25, 9, sqrt)'''

'''def format_name(s):
    return s[0].upper()+s[1:].lower()

print map(format_name, ['adam', 'LISA', 'barT'])'''
'''import math

def is_sqr(x):
    return math.sqrt(x) == int(math.sqrt(x))

print filter(is_sqr, range(1, 101))'''

'''def cmp_ignore_case(s1, s2):
    if s1.lower() > s2.lower():
        return 1
    if s1.lower() < s2.lower():
        return -1
        return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)'''

'''def f():
    print 'call f()...'
    # 定义函数g:
    def g():
        print 'call g()...'
    # 返回函数g:
    return g

x=f()
print f()()'''

'''def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum
f=calc_sum([1, 2, 3, 4])
print f()'''
'''def count():
    fs = []
    for i in range(1, 4):
        def f(i):
             return lambda: i*i
        fs.append(f(i))
        print f(i)()
    return fs

f1, f2, f3 = count()
print f1(),f2(),f3()'''
'''闭包
def count():
    fs = []
    for i in range(1, 4):
        def f(i):
            #g
            def g():
                return i*i
            #
            return g
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()'''

'''匿名函数lambda
is_not_empty = lambda s: s and len(s.strip())>0
print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])

print filter(lambda s: s and len(s.strip())>0, ['test', None, '', 'str', '  ', 'END'])'''
# 装饰器

'''def new_fn(f):
    def fn(x):
        print 'call ' + f.__name__ + '()'
        return f(x)
    return fn

def f1(x):
    return x*2

print "-----------------------------"
new_fn(f1)(5)'''

'''import time


def performance(f):
    def fn(*args,**kw):
        t1 = time.time()
        r = f(*args,**kw)
        # for i in range(1,1000000):
            # pass
        t2=time.time()
        print 'call %s() in %fs' % (f.__name__, (t2-t1))
        return r
    return fn


@performance
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))

print factorial(10)'''
'''import os.path
print os.path.isdir(r'/data/webroot/resource')
print os.path.isfile(r'/data/webroot/resource/python/test.txt')'''
'''try:
    import json
except ImportError:
    import simplejson as json
print json.dumps({'python':2.7})'''

'''from __future__ import unicode_literals

s = 'am I an unicode?'
print isinstance(s, unicode)'''
