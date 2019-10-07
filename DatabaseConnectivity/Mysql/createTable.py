import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost", user="root", passwd="Ransom@006", database="mysql")
    cur = conn.cursor()
    try:
        cur.execute("use pytab")
        cur.execute(
            "create table student(id int not null,name varchar(20) not null)")
    except Exception:
        print("cant create :(")

except Exception:
    print("Connection Error:(")
conn.close()
