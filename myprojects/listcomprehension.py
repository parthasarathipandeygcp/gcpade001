mylist=[x for x in 'abcde']
print(mylist)

mylist=[num**2 for num in range(1,10) if num%2==0]
print(mylist)

mylist=[]

for x in [1,2,3]:
    for y in [10,100,200]:
      mylist.append(x*y)
print(mylist)


word='my name is upendar Konda'
for i in word.split():
    if i[0].lower() == 'k':
     print(i)

for i in range(1,11):
    if i % 2 == 0:
     print(i)

word1=[i for i in range(1,51) if i % 3 == 0]
print(word1)

word='my name is upendar Konda'
for i in word.split():
    if len(i) % 2 == 0:
     print(i,'even')

word='my name is upendar Konda'
word1=[i[0] for i in word.split()]
print(word1)