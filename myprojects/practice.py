import mysql.connector

mydb=mysql.connector.connect(
    host="35.200.219.211",
    user="upendar",
    password="Upendar@123",
    database="upendar_database"
)


mycursor=mydb.cursor()

sql="show tables"
sql="create table employees(employeNum varchar(200), lastname varchar(200), firstname varchar(200),extension varchar(200),\
    email varchar(200), officecode varchar(200), reportsTo varchar(200), jobtitle varchar(200))"
sql="insert into employees (employeNum,lastname,firstname,extension,email,officecode,reportsTo,jobtitle)\
    values(%s,%s,%s,%s,%s,%s,%s,%s)"
val=[('11103580','konda','upendar','0803', 'kondaupendar11@gmail.com','100','Abdul','SSE'),
     ('11103581','konda','harini','0803', 'kondaharini11@gmail.com','101','Abdul','TL')]
mycursor.executemany(sql,val)
mydb.commit()
mycursor.execute("select * from employees")
myresult=mycursor.fetchall()
for i in myresult:
    print(i)


sql="delete database"
mycursor.execute(sql)
for i in mycursor:
    print(i)