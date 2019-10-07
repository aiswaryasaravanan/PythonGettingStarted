import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost", user="root", passwd="Ransom@006", database="pytab")
    cur = conn.cursor()
    try:
        cur.execute("insert into student values(1,'Aishu','CSE')")
    except Exception:
        print("cant insert :(")

except Exception:
    print("Connection Error:(")
# conn.close()
