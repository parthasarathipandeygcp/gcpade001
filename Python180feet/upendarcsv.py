import csv
projectpath = "c:/Users/LENOVO/myproject/gcpade001/"
datapath=projectpath+"/data"

#read
f=open(datapath+"/myfile.txt",'r')
#print(f.read())
for i in f:
 print(i)
f.close()

#write
f=open(datapath+"/upendar.txt",'w+')
f.write("my name is upendar")
for i in f:
 print(i)
f.close()

#adding
f=open(datapath+"/upendar.txt",'a+')
f.write("my name is konda \r")
for i in f:
 print(i)
f.close()

#delimiters csv files
f=open(datapath+"/innovators.csv",'r')
reader=csv.reader(f,delimiter="\t")
for i in reader:
 print(i)
f.close()

#delimiters csv files
f=open(datapath+"/mytest.csv",'r')
reader=csv.reader(f,delimiter="$")
for i in reader:
 print(i)
f.close()

#delimiters csv files with dict
f=open(datapath+"/mytest.csv",'r')
reader=csv.DictReader(f,delimiter="$")
for i in reader:
 print(i)
f.close()





