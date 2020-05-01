def name_fun():
    print('hello')
name_fun()

def name_fun(name):
    print('hello '+name)
name_fun('upendar')

def name_fun(name='konda'):
    print('hello '+name)
name_fun()

def name_fun(name='konda'):
    return 'hello '+name
new=name_fun('goud')
print(new)


def add(n1,n2):
 return n1+n2
new=add(20,30)
print(new)

def check(string):
    return 'dog' in string
new=check('the dog is in home')
print(new)


def myfunc(a):
 if a == 30:
     return 'Hello'
 elif a == 150:
     return "GoodBye"
new=myfunc(150)
print(new)

def myfunc(x,y,z):
    if z == True:
     return x
    elif z ==False:
     return y
new=myfunc(10,20,True)
print(new)

