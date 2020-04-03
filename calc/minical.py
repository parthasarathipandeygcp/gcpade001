


number_1=float(input("Enter your first no: "))
number_2=float(input("Enter your second no: "))
print("If you want to do sum press 1")
print("If you want to do substruction press 2")
print("If you want to do multiplication press 3")
print("If you want to do division press 4")
print("If you want to exit press 0 ")
choice=int(input("Please enter your choice: "))

def dosum(a,b):
    result=a+b
    return result
def dosubstruction(a,b):
    result=a-b
    return result
def domultiplication(a,b):
    result=a+b
    return result
def dodivision(a,b):
    result=a/b
    return result
itr=1
while (choice >= 0):
    if (choice==1):
        result=dosum(number_1, number_2)
        print ("The result is :",result)
    elif (choice==2):
        result=dosubstruction(number_1, number_2)
        print("The result is :", result)
    elif (choice==3):
        result=domultiplication(number_1, number_2)
        print("The result is :", result)
    elif (choice==4):
        result=dodivision(number_1, number_2)
        print("The result is :", result)
    elif (choice==0):
        print("You choose to exit from this program")
        exit()
    else:
        print("Invalid Choice Please choose a option from below")
        print("If you want to do sum press 1")
        print("If you want to do substruction press 2")
        print("If you want to do multiplication press 3")
        print("If you want to do division press 4")
        print("If you want to exit press 0 ")

    choice = int(input("Please enter your choice: "))
    number_1 = float(input("Enter your first no: "))
    number_2 = float(input("Enter your second no: "))