mystring = "Hey buddy, wassup?"

print(mystring[-2:])

print(mystring[1:3])

print(mystring[::-1])


data = {"A" : ["John","Deep","Julia","Kate","Sandy"],
                     "MonthSales" : [25,30,35,40,45]}

print(data)

for i in range(1,10,2):
    print(i)



lis = [100, 1, 10, 2, 3, 5, 8, 13, 21, 34, 55, 98]
#Output: [1, 10, 2, 3, 5, 8]
new=[]
for i in lis:
    if i>0 and i<=10:
     new.append(i)
print(new)


aaa="abcdef"
for i in aaa:
    if i =="a" or i =="d":
       continue
    print("letter :", i)

bbb="abcdef"
for i in bbb:
    if i =="c" or i =="d":
       break
    print("letter :", i)

i=1
while i < 10:

    i = i + 2
    print("new i :", i)

