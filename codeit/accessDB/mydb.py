import mysql.connector

mydb = mysql.connector.connect(
  host="35.200.219.211",
  user="partha",
  passwd="Partha@123"
  database="classicmodels"
)

print(mydb)
