import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", passwd="Ransom@006", database="mysql")
print(conn)
cur = conn.cursor()
print(cur)
try:
    cur.execute("create database pytab")
    print("yes")
    dbres = cur.execute("show databases")
except Exception:
    print("chorry:(")
    print(Exception)
for i in cur:
    print(i)
