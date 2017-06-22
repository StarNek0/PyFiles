f = open('imooc.txt')
iter_f = iter(f)
lines = 0
for line in iter_f:
    lines += 1
print lines

f.close()
