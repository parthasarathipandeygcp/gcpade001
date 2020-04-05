
projectpath='c:/Users/822024/myproject/gcpade001/'
# Open a file to read
def readfullfile(myfile):
    f= open(myfile,"r")
    print(f.read())
    f.close()
# Read a File line by line
def readfile(myfile):
    f= open(myfile,"r")
    for each in f: 
        print (each) 
    f.close() 
# Create a Text File and write data in the text file

def writfile(myfile):
    f= open(myfile,"w+")
    for i in range(10):
        f.write("This is line %d\r" % (i+1)) 
    f.close() 


# Append data in the text file
def appendfile(myfile):
    f= open(myfile,"a+")
    i=10
    for i in range(20):
        f.write("This is line %d\r" % (i+1)) 
    f.close() 

myfile=projectpath+"data/myfile.txt"
readfullfile(myfile)
readfile(myfile)

myfile=projectpath+"data/newfiletowrite.txt"
writfile(myfile)
readfile(myfile)
appendfile(myfile)
readfile(myfile)