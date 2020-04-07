import mysql.connector
import csv
#import datetime
mydb=mysql.connector.connect(
    host="35.200.219.211",
    user="upendar",
    password="Upendar@123",
    database="mydb_upendar"
)

mydb = mysql.connector.connect(
  host="35.200.219.211",
  user="partha",
  passwd="Partha@123"
)

print(mydb)

# List all the data bases in the dbserver

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

mycursor=mydb.cursor()
mycursor.execute("drop table Mytable")
sql="create table Mytable (job_name varchar(200), last_run varchar(200), lastrun_status varchar(200), dependent_job varchar(200))"
mycursor.execute(sql)
sql="insert into Mytable (job_name,last_run,lastrun_status, dependent_job) values(%s,%s,%s,%s)"
val=[('VS6: Clean MSEG (p02 & rbp)','2020-04-02 12:30:23','pass','NA'),
    ('VS6 DVSM Edge Assignment','2020-04-02 13:30:23','pass','NA'),
    ('VS6 DVSM Edge Assignment to Table','2020-04-02 14:30:23','pass','VS6 Clean MSEG (p02 & rbp)'),
    ('VS6 mount blob storage to DBFS','2020-04-02 15:30:23','fail','VS6 DVSM Edge Assignment to Table'),
    ('VS6 MSEG Event Linker 1/6','2020-04-02 16:30:23','pass','VS6 DVSM Edge Assignment to Table'),
    ('VS6 MSEG Event Linker 2/6','2020-04-02 16:30:23','pass','VS6 DVSM Edge Assignment to Table'),
    ('VS6 MSEG Event Linker 3/6','2020-04-02 16:30:23','fail','VS6 DVSM Edge Assignment to Table'),
    ('VS6 MSEG Event Linker 4/6','2020-04-02 17:45:23','pass','VS6 MSEG Event Linker 3/6'),
    ('VS6 MSEG Event Linker 5/6','2020-04-02 17:45:23','pass','VS6 MSEG Event Linker 3/6'),
    ('VS6 MSEG Event Linker 6/6','2020-04-02 17:45:23','unknown','VS6 mount blob storage to DBFS VS6 MSEG Event Linker 3/6'),
    ('VS6 SSO CX', '2020-04-02 19:45:23', 'pass', 'VS6 mount blob storage to DBFS VS6 MSEG Event Linker 3/6'),
    ('VS6 SSO Demand Forecast/Actual', '2020-04-02 20:45:23', 'unknown','VS6 DVSM Edge Assignment VS6 mount blob storage to DBFS VS6 MSEG Event Linker 3/6'),
    ('VS6 SSO RX', '2020-04-02 21:45:23', 'pass', 'VS6 mount blob storage to DBFS VS6 MSEG Event Linker 3/6'),
    ('VS6 email notification', '2020-04-02 21:45:23', 'unknown','VS6 DVSM Edge Assignment to Table VS6 SSO Demand Forecast/Actual')]
mycursor.executemany(sql,val)
mydb.commit()

#fail=mycursor.execute("select job_name, last_run,lastrun_status  from Mytable where lastrun_status in('fail','unknown') ")
#mycursor.execute(fail)
#myresult=mycursor.fetchall()
#for y in myresult:
    #print(y)


fail=mycursor.execute("select job_name, last_run,lastrun_status  from Mytable where lastrun_status='unknown'")
mycursor.execute(fail)
myresult=mycursor.fetchall()
for y in myresult:
    print(y)
    print("email notification failed")


