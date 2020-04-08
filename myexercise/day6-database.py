import mysql.connector


mydb = mysql.connector.connect(
  host="35.200.219.211",
  user="upendar",
  passwd="Upendar@123",
   database="MYDB_upendar"
)

print(mydb)

#offices table
mycursor = mydb.cursor()
sql="create table offices (officecode varchar(200), city varchar(200), phone varchar(200),addressline1 varchar(200),\
    addressline2 varchar(200),state varchar(200),country varchar(200), postalcode varchar(200), territory varchar (200))"
#mycursor.execute(sql)

sql="insert into offices (officecode,city,phone, addressline1,addressline2,state ,country,postalcode,territory)\
    values(%s, %s, %s, %s, %s, %s,%s, %s, %s)"

val=[('100','hyd','7680915878','4-102 chilkur','5-5-1105 lbnagar','telangana','india','508206','asia'),
     ('101','vij','7680915878','4-1102 vijayawada','5-5-1105 vijayawada','andrapradesh','india','508200','asia')]
#mycursor.executemany(sql,val)
mydb.commit()
mycursor.execute("select * from offices")
myresult=mycursor.fetchall()
for x in myresult:
  print(x)


#employees
mycursor = mydb.cursor()
sql="create table employees (employeNum varchar(200), lastname varchar(200), firstname varchar(200),extension varchar(200),\
    email varchar(200), officecode varchar(200), reportsTo varchar(200), jobtitle varchar(200))"
#mycursor.execute(sql)

sql="insert into employees (employeNum, lastname, firstname, extension, email, officecode ,reportsTo, jobtitle)\
    values(%s, %s, %s, %s, %s, %s,%s, %s)"

val=[('11103580','konda','upendar','0803', 'kondaupendar11@gmail.com','100','Abdul','SSE'),
     ('11103581','konda','harini','0803', 'kondaharini11@gmail.com','101','Abdul','TL')]
#mycursor.executemany(sql,val)
mydb.commit()
mycursor.execute("select * from employees")
myresult=mycursor.fetchall()
for x in myresult:
  print(x)


#customers
mycursor = mydb.cursor()
sql="create table customers (customerNum varchar(200), CustomerName varchar(200), Contactlastname varchar(200),Contactfirstname varchar(200),\
    phone varchar(200), addressline1 varchar(200),addressline2  varchar(200), city varchar(200), state varchar(200), \
    postalcode varchar(200),country varchar(200), SalesRepemployeeNum varchar(200), creditlimit varchar(200))"
#mycursor.execute(sql)

sql="insert into customers (customerNum, CustomerName, Contactlastname, Contactfirstname, phone, addressline1 ,addressline2, \
    city, state, postalcode, country, SalesRepemployeeNum, creditlimit) values(%s, %s, %s, %s, %s, %s,%s, %s,%s,%s,%s,%s,%s)"

val=[('ABC100','konda001','upendar','konda', '7680915878','72-canningstreet', '75-canningstreet',
       'hyd','telangana', '500072', 'india', 'Ashok', '5000'),
     ('ABC101', 'upendar001', 'upendar', 'konda', '7680915878', '72-canningstreet', '75-canningstreet',
      'hyd', 'telangana', '500072', 'india', 'Abdul', '10000')]
#mycursor.executemany(sql,val)
mydb.commit()
mycursor.execute("select * from customers")
myresult=mycursor.fetchall()
for x in myresult:
  print(x)



#productlines table
mycursor = mydb.cursor()
sql="create table productlines (productline varchar(200), textDescription varchar(200), htmldescription varchar(200),image varchar(200))"
#mycursor.execute(sql)

sql="insert into productlines (productline, textDescription, htmldescription, image) values(%s, %s, %s, %s)"

val=[('All100','allproductscombine','allproductscombine.html','cat'),
     ('All101','allproductscombine','allproductscombine.html','cat')]
#mycursor.executemany(sql,val)
mydb.commit()
mycursor.execute("select * from productlines")
myresult=mycursor.fetchall()
for x in myresult:
  print(x)



#products table
mycursor = mydb.cursor()
sql="create table products (productcode varchar(200), productName varchar(200), productline varchar(200),productscale varchar(200), \
    productvendor varchar(200), productDescription varchar(200), quantityinStock varchar(100),buyprice varchar(200),MSRP varchar(100))"
#mycursor.execute(sql)

sql="insert into products (productcode, productName, productline, productscale, productvendor, productDescription, \
    quantityinStock, buyprice, MSRP) values(%s, %s, %s, %s,%s, %s, %s, %s,%s)"

val=[('ABCD','soap','All100','low','santhoor','bodysoap','5000','50','100'),
     ('EFGH','paste','All101','high','colgate','toothpaste','5000','50','100')]
#mycursor.executemany(sql,val)
mydb.commit()
mycursor.execute("select * from products")
myresult=mycursor.fetchall()
for x in myresult:
  print(x)



#orderdetails table
mycursor = mydb.cursor()
sql="create table orderdetails (OrderNum varchar(200), productcode varchar(200), quantityOrderred  varchar(200),priceEach varchar(200), \
    orderLineNumber varchar(200))"
#mycursor.execute(sql)

sql="insert into orderdetails (OrderNum, productcode, quantityOrderred, priceEach, orderLineNumber) values(%s, %s, %s, %s,%s)"

val=[('000001','ABCD','10000','50','1000'),
     ('000002','EFGH', '50000','60','1001')]
#mycursor.executemany(sql,val)
mydb.commit()
mycursor.execute("select * from orderdetails")
myresult=mycursor.fetchall()
for x in myresult:
  print(x)



#orders table
mycursor = mydb.cursor()
sql="create table orders (OrderNum varchar(200), orderdate varchar(200), requireddate  varchar(200), shippeddate varchar(200), \
    status varchar(200), comments varchar(200), customerNum varchar(200))"
#mycursor.execute(sql)

sql="insert into orders (OrderNum, orderdate, requireddate, shippeddate, status, comments, customerNum) values(%s, %s, %s, %s,%s, %s,%s)"

val=[('000001','23/07/2018','23/08/2018','01/09/2018','shipped','looking for new pdt','ABC100'),
     ('000002','23/07/2019','23/08/2019','01/09/2019','shipped','looking for new pdt','ABC101')]
#mycursor.executemany(sql,val)
mydb.commit()
mycursor.execute("select * from orders")
myresult=mycursor.fetchall()
for x in myresult:
  print(x)



#payments table
mycursor = mydb.cursor()
sql="create table payments (customerNum varchar(200), checkNum varchar(200), paymentdate  varchar(200), amount varchar(200))"
#mycursor.execute(sql)

sql="insert into payments (customerNum, checkNum, paymentdate, amount) values(%s, %s, %s, %s)"

val=[('ABC100','000999','25/08/2018','25000'),
     ('ABC101','000119','25/08/2019','60000')]
#mycursor.executemany(sql,val)
mydb.commit()
mycursor.execute("select * from payments")
myresult=mycursor.fetchall()
for x in myresult:
  print(x)




#Write code to display  office address of all employees
sql="select employees.employeNum, employees.lastname, employees.firstname, employees.extension\
            ,employees.email, employees.officecode ,employees.reportsTo, employees.jobtitle\
            ,offices.city,offices.phone, offices.addressline1,offices.addressline2 \
            ,offices.state ,offices.country,offices.postalcode,offices.territory\
            from employees  \
            inner join offices \
            on employees.officecode=offices.officecode"

mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
  print(x)



#Write a code to display the customer name, product he/she ordered and the shipping date
sql= "select customers.CustomerName\
            ,products.productName\
            ,orders.shippeddate\
            from customers\
            inner join orders\
            on customers.customerNum=orders.customerNum\
            inner join orderdetails\
            on  orders.OrderNum=orderdetails.OrderNum\
            inner join products\
            on  products.productcode=orderdetails.productcode"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)