# connect to mysqldb
#coding:utf-8
import MySQLdb

conn = MySQLdb.Connect(host='127.0.0.1', port=3306, user='root', passwd='klxsxzsdf1', db='imooc', charset='utf8')
cursor = conn.cursor()

print conn
print cursor

cursor.close()
conn.close()
