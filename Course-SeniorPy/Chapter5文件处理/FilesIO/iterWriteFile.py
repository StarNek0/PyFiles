# coding:utf8
with open('imooc.txt', 'w') as f:
    f.write('imooc')

f = open('imooc.txt', 'r')
print f.read()
f.close()

# f.tell()
# f.seek(0, os.SEEK_CUR)  # 偏移量，指针在当前位置
# f.seek(0, os.SEEK_SET)  # 起始位置
# f.seek(0, os.SEEK_END)  # 结尾位置


from ConfigParser import ConfigParser  # 这个库可以怼ini文件

cfg = ConfigParser()
print cfg.read('inini.txt')

print cfg.sections()
cfg.set('userinfo', 'pwd', '12345678')
print '-------------------------------------------------------------------------------'
for i in cfg.sections():
    print i
    print cfg.items(i)
    print '-------------------------------------------------------------------------------'
