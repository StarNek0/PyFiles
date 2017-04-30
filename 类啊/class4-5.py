# coding:utf8
# 不明觉厉系列


class Programer(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, name):
        # return getattr(self, name)
        # return self.__dict__[name]
        return super(Programer,self).__getattribute__(name)

    def __getattr__(self, name,value):
        self.__dict__[name] = value

if __name__ == '__main__':
    p = Programer('Albert',25)
    print p.name