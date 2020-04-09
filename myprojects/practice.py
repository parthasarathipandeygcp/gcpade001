a=2

for i in range(1,11):
    print(a,'X',i,'=',a*i)

a=2
b=10

temp=a
a=b
b=temp

print('swap values are:',a,b)

# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

a=int(input("enter num:"))

if a%2==0:
    print("even")

else:
    print('odd')


# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

sum=0

for i in numbers:
    sum=i+sum
    print(sum)
