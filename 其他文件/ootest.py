#coding:utf-8
'''class Person:
    def __init__(self, name):
        self.name = name
p1 = Person('Xiao Ming')
p2 = Person('Xiao Jun')
p3 = Person('Xiao Hong')
'''


'''class Person(object):
    def __init__(self,):
        pass

xiaoming = Person()
xiaohong = Person()

print xiaoming
print xiaohong
print xiaoming == xiaohong'''

'''Person(object):
    pass
def cmp1(x, y):
    return cmp(x.name, y.name)

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1,lambda x,y:cmp(x.name, y.name))

print L2[0].name
print L2[1].name
print L2[2].name'''

#要定义关键字参数，使用 **kw；

#除了可以直接使用self.name = 'xxx'设置一个属性外，还可以通过 setattr(self, 'name', 'xxx') 设置属性。
'''
class Person(object):
    def __init__(self, name, gender, birth, **kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        for i, j in kw.iteritems():
            setattr(self, i, j)
xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print xiaoming.name
print xiaoming.job
'''


# 请给Person类的__init__方法中添加name和score参数，并把score绑定到__score属性上，看看外部是否能访问到。
'''class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

p = Person('Bob', 59)

print p.name
try:
    print p.__score
except AttributeError:
    print "attributeError:"'''

'''由类属性创建的实例，修改实例的类属性，实例属性改变，而类属性不变
class Hello(object):
    ajp = 'dasd'
hel = Hello()
print Hello.ajp
print hel.ajp
hel.ajp = 'qweqweqw'
print hel.ajp
print Hello.ajp'''

'''
class Person(object):
    count =0
    def __init__(self,name):
        self.name = name
        Person.count += 1

p1 = Person('Bob')
print Person.count

p2 = Person('Alice')
print Person.count

p3 = Person('Tim')
print Person.count'''


'''class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person('Bob', 90)
print p1.get_grade
print p1.get_grade()'''


'''class Person(object):

    __count = 0

    @classmethod
    def how_many(cls):
        return cls.__count

    def __init__(self, name):
        self.name = name
        Person.__count += 1#此处不用self. 不知道为什么::可能是因为__count was defined in the Class rather than in Function

print Person.how_many()

p1 = Person('Bob')

print Person.how_many()'''


