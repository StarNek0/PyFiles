def poww(a, b):
    if a == 0:
        return 0
    if b == 0:
        return 1

    sum_pow = 1
    for i in range(b):
        sum_pow = sum_pow * a
    return sum_pow

for n in range(1001):
    print poww(n, n)
