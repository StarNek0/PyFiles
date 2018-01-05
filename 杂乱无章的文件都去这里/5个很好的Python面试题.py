# coding:utf8
"""
-------------------------------------------------
    File:   5个很好的Python面试题.py
    Auth:   zsdostar
    Date:   2017/11/19 21:14
    Sys:    Windows 10
-------------------------------------------------
    Desc:   http://python.jobbole.com/86525/
            的Python练习题
            其中标记*的第四题涉及lambda，比较难
            第五题涉及了函数的默认参数与list
-------------------------------------------------
"""
__author__ = 'zsdostar'


def div1(x, y):
    print("%s/%s = %s" % (x, y, x / y))


def div2(x, y):
    print("%s//%s = %s" % (x, y, x // y))


div1(5, 2)
div1(5., 2)
div2(5, 2)
div2(5., 2.)
"""以上的代码的输出将是什么? 说出你的答案并解释？"""

"""以下代码将输出什么?"""
lst = ['a', 'b', 'c', 'd', 'e']
print lst[10:]


"""****************以下的代码的输出将是什么? 说出你的答案并解释?****************"""


def multipliers():
    return [lambda x: i * x for i in range(4)]


print [m(2) for m in multipliers()]

"""以上代码的输出是 [6, 6, 6, 6] （而不是 [0, 2, 4, 6]）。
这个的原因是 Python 的闭包的后期绑定导致的 late binding，这意味着在闭包中的变量是在内部函数被调用的时候被查找。所以结果
是，当任何 multipliers() 返回的函数被调用，在那时，i 的值是在它被调用时的周围作用域中查找，到那时，无论哪个返回的函数被
调用，for 循环都已经完成了，i 最后的值是 3，因此，每个返回的函数 multiplies 的值都是 3。因此一个等于 2 的值被传递进以上
代码，它们将返回一个值 6 （比如： 3 x 2）。

最普遍的解决方案是创建一个闭包，通过使用默认参数立即绑定它的参数。例如：
改成如下就好了

def multipliers():
    return [lambda x, i=i : i * x for i in range(4)]
"""


"""以下的代码的输出将是什么? 说出你的答案并解释？"""


def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3

"""
实际发生的事情是，新的默认列表仅仅只在函数被定义时创建一次。随后当 extendList 没有被指定的列表参数调用的时候，其使用的是同一个列表。
因此，list1 和 list3 是操作的相同的列表。而 list2是操作的它创建的独立的列表（通过传递它自己的空列表作为list 参数的值）。

def extendList(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list
"""