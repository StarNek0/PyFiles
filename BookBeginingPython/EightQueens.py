# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/4/30 21:00'
__doc__ = '''以下为《Begining Python》书第九章末尾的代码实现-八皇后问题'''


def conflict(state, next_x):
    next_y = len(state)
    for i in range(next_y):
        if abs(state[i]-next_x) in (0, next_y-i):
            return True
    return False


def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num, state+(pos,)):
                    yield (pos, ) + result


def prettyprint(solution):
    # 函数内部的函数为助手函数
    def line(pos, length=len(solution)):
        return '. '*pos+'* '+'. '*(length-pos-1)
    for pos in solution:
        print line(pos)
print len(list(queens(8)))
prettyprint(list(queens(8))[1])
