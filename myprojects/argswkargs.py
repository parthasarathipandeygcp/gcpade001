def mydef(a,b,c=0,d=0):
    return sum((a,b))
new=mydef(10,20)
print(new)

def mydef(*args):
    print(args)
    return sum((args))
new=mydef(10,20,30,40,50,100)
print(new)

def mydef(**kwargs):
    print(kwargs)
    return ('mychoice of fruit is {}  '.format(kwargs['fruit']))
new=mydef(fruit='apple',veggi='broccli')
print(new)



def mydef(*args,**kwargs):
    print(args)
    print(kwargs)
    return ('i  like {} {}'.format(args[1],kwargs['fruit']))
new=mydef(10,20,30,fruit='oranges',veggi='spinash')
print(new)


def mydef(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
new=mydef(2,5)
print(new)

def mydef(txt):

    wordlist=txt.split()
    return wordlist[0][0]==wordlist[1][0]
new=mydef('upendar ude')
#new=mydef('konda op')
print(new)

def mydef(txt):
   return txt[0].upper() + txt[1:3] + txt[3].upper() + txt[4:]
new=mydef('macdonald')
print(new)

def mydef(txt):
   return txt[0:3].capitalize() + txt[3:].capitalize()
   new=mydef('macdonald')
print(new)


def mydef(txt):
    wordtxt=txt.split()
    return '    '.join(wordtxt[::-1])
new=mydef('i am at home')
print(new)


def mydef(*x):
   for i in range(0,len(x)-1):
       if x[i]==3 and x[i+1]==3:
           return True
   return False
new=mydef(1,3,3)
print(new)

def mydef(txt):
    result=''
    for i in txt:
     result += i*3
    return result
new=mydef('konda')
print(new)

