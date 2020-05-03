hungry=True
if hungry:
    print('feed me')
else:
    print('i am not hungry')


loc='hyd'
if loc=='vij':
    print('vijayawada')
elif loc=='mum':
    print('munmbai')
else:
    print('hyderabad')

mylist=[1,2,3,4,5,6,7,8,9,10]

for i in mylist:
    if i % 2== 0:
     print(i)
    else:
        print(f'odd number',{i})

sum=0
for i in mylist:
    sum=sum+i
print(sum)

mylist=[(1,2),(2,3),(3,4),(4,5)]
for i in mylist:
    print(i)

mylist=[(1,2),(2,3),(3,4),(4,5)]
for a,b in mylist:
    print(a)
    print(b)

d = {'k1':1, 'k2':3,'k3':5}
for i in d.items():
     print(i)

d = {'k1':1, 'k2':3,'k3':5}
for key,values in d.items():
     print(key)

d = {'k1':1, 'k2':3,'k3':5}
for key,values in d.items():
     print(values)