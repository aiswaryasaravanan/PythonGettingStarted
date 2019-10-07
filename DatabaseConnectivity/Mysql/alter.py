import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost", user="root", passwd="Ransom@006", database="pytab")
    cur = conn.cursor()
    try:
        cur.execute("alter table student add column dept varchar(10)")
    except Exception:
        print("cant alter :(")

except Exception:
    print("Connection Error:(")
# conn.close()
