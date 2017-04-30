# run sql from mysql to python using cursor
#coding:utf-8
import MySQLdb

conn = MySQLdb.Connect(host='127.0.0.1', port=3306, user='root', passwd='klxsxzsdf1', db='imooc', charset='utf8')
cursor = conn.cursor()

print conn
print cursor

sql = 'select * from user;'
cursor.execute(sql)

print cursor.rowcount

rs = cursor.fetchone()
print rs

rs = cursor.fetchmany(3)
print rs

rs = cursor.fetchall()
print rs

cursor.close()
conn.close()
