# -*- coding: gb2312 -*-
#author 6x0cm
#website www.06m.me
#use:md5.py host user pass database table md5(32位)
import pymysql
import sys

def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

mysql_host = sys.argv[1]
mysql_user = sys.argv[2]
mysql_pass = sys.argv[3]
mysql_data = sys.argv[4]
mysql_table = sys.argv[5]
find_md5 = sys.argv[6]

db =pymysql.connect(mysql_host,mysql_user,mysql_pass,mysql_data)
cursor = db.cursor()
query = cursor.execute("select password from " + mysql_table)
info = cursor.fetchmany(query)
#print info
cursor.close()
db.commit()
db.close()

flag = False
for ii in info:
    try:
        data = ii[0].replace('\r', '')
        password = md5("laoy"+data)
#        password = md5(data)
        if password == find_md5:
            print "匹配出的明文" + ii[0]
            flag = True
    except:
        pass
if not flag:
    print "无匹配结果!"
