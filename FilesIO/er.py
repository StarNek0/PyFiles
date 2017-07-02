import os
try:
    f = open('1.txt')
    line = f.read(2)
    f.seek(-5, os.SEEK_SET)
    # num = int(line)
    # print 'read num=%d' % num
except IOError as e:
    print 'catch IOError:', e
except ValueError as e:
    print 'catch ValueError:', e
except IndexError as e:
    print 'catch IndexError', e
else:
    print 'No Error'
finally:
    print 'finally!'
    try:
        print 'close.file'
        f.close()
    except NameError as e:
        print 'catch Error:', e

print '----------------------------------------------------'

with open('1.txt') as f1:
    print 'in with f.read:', f1.read()
    f1.seek(-5, os.SEEK_SET)


print 'with:', f.closed
