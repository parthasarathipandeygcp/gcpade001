import mysql.connector
mydb = mysql.connector.connect(
  host="35.200.219.211",
  user="upendar",
  passwd="Upendar@123",
  database="upendar_db"
)

print(mydb)


mycursor=mydb.cursor()
#sql=mycursor.execute("drop table new")
sql="create table new (name varchar(100), address(20))"
#mycursor.execute(sql)
mycursor.execute("show tables")
for i in mycursor:
    print(i)
sql="insert into new (name, address) values (%s,%s)"
val=[('jha','sur')]
mycursor.executemany(sql,val)


mydb.commit()
"""
sql="select * from new \
         
mycursor.execute("select * FROM new  LIMIT 5")
myresult=mycursor.fetchall()
for i in myresult:
     print(i)
"""



