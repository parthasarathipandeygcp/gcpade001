mydb = mysql.connector.connect(
  host="35.200.219.211",
  user="partha",
  passwd="Partha@123"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
