# module needed for connecting mysql is mysql-connector
# pip install mysql-connector
import mysql.connector


# Code to connect a data base
# Please note each student has a user by their name and the password is their name in initcap with an additional @123
#if the student name is Abdul then the user name = abdul and password = Abdul@123

# Connect the database server
"""
mydb = mysql.connector.connect(
  host="35.200.219.211",
  user="partha",
  passwd="Partha@123",
)

print(mydb)

# List all the data bases in the dbserver

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


# Create a database 

mycursor.execute("CREATE DATABASE mydatabase_partha")
# Connect to a specific database
"""
mydb = mysql.connector.connect(
  host="35.200.219.211",
  user="partha",
  passwd="Partha@123",
  database="mydatabase_partha"
)

mycursor = mydb.cursor()

#Show the lists of tables

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

#create a table

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

# Drop table
mycursor.execute("DROP TABLE customers ")

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

# Create table with constarints
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
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
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


#Select all records from the "customers" table, and display the result:

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


#Select only the name and address columns:

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Select record(s) where the address is "Park Lane 38": result:

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Select records where the address contains the word "way":

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Escape query values by using the placholder %s method:

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Sort the result alphabetically by name: result:

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


#Delete any record where the address is "Mountain 21":

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")


#Escape values by using the placeholder %s method:

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

#Overwrite the address column from "Valley 345" to "Canyoun 123":

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")


#Escape values by using the placholder %s method:

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")


#Select the 5 first records in the "customers" table:

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Join users and products to see the name of the users favorite product:

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)