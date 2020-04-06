import mysql.connector


mydb=mysql.connector.connect(
    host="35.200.219.211",
    user="upendar",
    password="Upendar@123",
    database="mydb_upendar"

)

print(mydb)

mycursor=mydb.cursor()
mycursor.execute("drop table emp")
sql="create table emp (name varchar(200), address varchar(300))"
mycursor.execute(sql)

mycursor.execute("show tables")
for y in mycursor:
    print(y)


sql="insert into emp (name,address) values('upendar', 'banglore')"
mycursor.execute(sql)
mydb.commit()
mycursor.execute("select * from emp")
myresult=mycursor.fetchall()
for i in myresult:
    print(i)


sql="select * from employee"
mycursor.execute(sql)
for i in mycursor:
    print(i)


sql="select a.* \
    b.* \
    from employee as a\
    inner join emp as b\
    on a.name=b.name"

mycursor.execute(sql)
for i in mycursor:
    print(i)


