index_count=0
word='abcde'
for i in word:
    print('at index {} the letter is {}'.format(index_count,i))
    index_count=index_count+1


word='abcd'

for index,letter in enumerate(word):
    print(index)
    print(letter)


mylist=[1,2,3,4]
mystring=['a','b','c','d']
new=zip(mylist,mystring)
for i in new:
 print(i)

from random import shuffle
mylist=[1,2,3,4]
shuffle(mylist)
print(mylist)

#new=float(input('enter a num:'))
#print(new)
