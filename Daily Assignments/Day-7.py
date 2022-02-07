# Day 7 Assignment - Python Database Connection Project which updates any one value in the table and select all the table data and print it.

import mysql.connector as sql           # importing module

# Connecting the local mysql database
database = sql.connect(host = 'localhost', user = 'root', passwd = 'ferrari458', database = 'schooldata')

cur = database.cursor()


cur.execute("update student set Eng_mark = 80 where Roll_no = 122")     # Update the record 
cur.execute("select * from student")        # View the table

for i in cur:
    print(i)

cur.close()
database.commit()       # commit changes or save changes.
