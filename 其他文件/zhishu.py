# coding:utf8
# __envirment__ = '网吧'
__doc__ = "求出最小的50个质数"
count = 1
l = [2, ]
for i in range(3, 1000)[::2]:
    if count >= 50:
        break
    for x in range(2, i):
        if i % x == 0:
            break
        if i % x != 0 and x == i - 1:
            l.append(i)
            count += 1
for i, x in enumerate(l):
    print x,
    if (i + 1) % 5 == 0:
        print '\n',
