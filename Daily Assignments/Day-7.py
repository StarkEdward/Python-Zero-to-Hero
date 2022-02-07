
import mysql.connector as sql

database = sql.connect(host = 'localhost', user = 'root', passwd = 'ferrari458', database = 'schooldata')

cur = database.cursor()


cur.execute("update student set Eng_mark = 80 where Roll_no = 122")
cur.execute("select * from student")

for i in cur:
    print(i)

cur.close()
database.commit()
