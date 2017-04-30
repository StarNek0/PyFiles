# connect to mysqldb
# coding:utf-8
import MySQLdb

conn = MySQLdb.Connect(host='127.0.0.1', port=3306, user='root', passwd='klxsxzsdf1', db='imooc', charset='utf8')
cursor = conn.cursor()

sql_insert = "insert into user(username) values ('name10');"
sql_update = "update user set username = 'name91' where userid=9;"
sql_delete = "delete from user where userid<3;"

try:
    cursor.execute(sql_insert)
    print cursor.rowcount

    cursor.execute(sql_update)
    print cursor.rowcount

    cursor.execute(sql_delete)
    print cursor.rowcount
    # 在此处执行发现三条语句并没有提交到mysql，这是因为没有commit事物，以下
    conn.commit()
except Exception as e:
    print e
    conn.rollback()  # 出错回滚数据

cursor.close()
conn.close()
