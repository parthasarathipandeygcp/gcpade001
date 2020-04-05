import csv
projectpath="C:/Users/LENOVO/myproject/gcpade001"
datapath=projectpath+"/data"

#f=open(datapath+"/upendar.txt","a+")
#f.write("hi my name is upendar \r")
#f.close()


f=open(datapath+"/person.csv","r")
reader=csv.reader(f)
for i in reader:
    print(i)

with open(datapath+"/mytest.csv","r") as f:
    reader = csv.reader(f,delimiter='$')
    for i in reader:
        print(i)


