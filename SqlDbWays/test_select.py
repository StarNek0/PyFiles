# connect to mysqldb
#coding:utf-8
import MySQLdb

conn = MySQLdb.Connect(host='127.0.0.1', port=3306, user='root', passwd='klxsxzsdf1', db='imooc', charset='utf8')
cursor = conn.cursor()

sql = 'select * from user;'
cursor.execute(sql)

rs = cursor.fetchall()  # 从mysql客户端缓冲区读取数据到rs
for row in rs:
    print 'userid=%s, username=%s' % row

cursor.close()
conn.close()
