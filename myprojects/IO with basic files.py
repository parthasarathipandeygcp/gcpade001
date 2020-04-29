myfile=open('country.txt')
print(myfile.read())
myfile.close()


#with open('country.txt',mode='r') as myfile:
#   print(myfile.read())

with open('country.txt',mode='a') as f:
    print(f.write("'IN':'INDIAN'"))

