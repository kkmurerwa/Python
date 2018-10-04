"""import
db = mysqlx.connect(host="localhost", user="root",passwd="toor",db="pythonlogin")
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM login")

# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[0])
db.close"""

import pymysql
import pymysql.cursors
from tkinter import  messagebox

conn = pymysql.connect(host='localhost',user='root',password='toor',db='pythonlogin',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
a=conn.cursor()


if conn:
    messagebox.showinfo("success","Connection successful")