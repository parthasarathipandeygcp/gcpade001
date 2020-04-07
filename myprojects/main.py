from myprojects.division import division
from myprojects.multiplication import multiplication
from myprojects.sum import sum
from myprojects.substruction import substruction

number_1=float(input("Enter your first no: "))
number_2=float(input("Enter your second no: "))
print("If you want to do sum press 1")
print("If you want to do substruction press 2")
print("If you want to do multiplication press 3")
print("If you want to do division press 4")
print("If you want to exit press 0 ")
choice=int(input("Please enter your choice: "))

itr=1
while (choice >= 0):
    if (choice==1):
        result=sum(number_1, number_2)
        print ("The result is :",result)
    elif (choice==2):
        result=substruction(number_1, number_2)
        print("The result is :", result)
    elif (choice==3):
        result=multiplication(number_1, number_2)
        print("The result is :", result)
    elif (choice==4):
        result=division(number_1, number_2)
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