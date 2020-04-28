a="this is a string {} "
print(a.format("inserted"))

a="i am {} {} {}"
print(a.format('upendar', 'konda','goud'))

a="i am {2} {0} {1}"
print(a.format('upendar', 'konda','goud'))

a="i am {0} {0} {0}"
print(a.format('upendar', 'konda','goud'))

a="i am {k} {u} {g}"
print(a.format(u='upendar', k='konda',g='goud'))

name='upendar'
age=34
print(f'{name} is {age} years old')

a='i like {}'
print(a.format('apples'))




