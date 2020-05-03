a=['one','two','three']
print(a[0])

n_list = ["Happy", [2,0,1,5]]
print(n_list[0][1])

n_list = ["Happy", [2,0,1,5]]
n_list.append('up')
print(n_list)

a=['one','two','three']
new=a.pop(0)
new=a.pop()
print(a)

a=['z','x','y','a','b']
a.sort()
new_sort=a
print(new_sort)

a.reverse()

print(a)


dict={'apples':100,'oranges':200,'grapes':300}
print(dict['apples'])

new={'k1':100,'k2':[1,2,3],'k3':{'insidekey':300}}
print(new['k1'])
print(new['k2'][2])
print(new['k3']['insidekey'])

d={'key1':['a','b','a']}
print(d['key1'][2].upper())

dic={'k1':100,'k2':300}
dic['k3']=400
dic['k1']=500
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())

tup=(1,2,3,2,2)
print(tup.count(2))
print(tup.index(3))
print(tup.index(2))








