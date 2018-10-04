import pymysql
import pymysql.cursors
name = "kenneth"
conn = pymysql.connect(host='localhost',user='root',password='toor',db='pythonlogin',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
a=conn.cursor()
a.execute("SELECT password FROM login where username = '" + name + "'")
for row in a.fetchall():
    print(row)