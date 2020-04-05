import mysql.connector


mydb=mysql.connector.connect(
    host="35.200.219.211",
    user="upendar",
    password="Upendar@123",
    database="mydb_upendar"

)

print(mydb)

mycursor=mydb.cursor()
mycursor.execute("drop table employee")
sql="create table employee (name varchar(200), address varchar(300))"
mycursor.execute(sql)

mycursor.execute("show tables")
for y in mycursor:
    print(y)

sql="insert into employee (name,address) values('upendar', 'hyderabad')"

#mycursor.execute(sql)
sql="insert into employee (name,address) values(%s,%s)"
val=[('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')]
mycursor.executemany(sql,val)
mydb.commit()
mycursor.execute("select * from employee")

myresult = mycursor.fetchall()
for i in myresult:
    print(i)

