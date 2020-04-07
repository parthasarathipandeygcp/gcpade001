import mysql.connector
import csv
#import datetime
mydb=mysql.connector.connect(
    host="35.200.219.211",
    user="upendar",
    password="Upendar@123",
    database="mydb_upendar"
)
mycursor=mydb.cursor()
mycursor.execute("drop table Mytable")
sql="create table Mytable (job_name varchar(200), last_run varchar(200), lastrun_status varchar(200), dependent_job varchar(200))"
mycursor.execute(sql)

mycursor.execute("show tables")
for y in mycursor:
    print(y)



projectpath = "c:/Users/LENOVO/myproject/gcpade001/"
datapath=projectpath+"/data"

f=open(datapath+"/jobs.csv")
reader=csv.reader(f,delimiter='|')
columns = next(reader)
query = 'insert into Mytable({0}) values ({1})'
query = query.format(','.join(columns), ','.join('?' * len(columns)))
mycursor.executemany(query,columns)
mydb.commit()
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
f.close()


