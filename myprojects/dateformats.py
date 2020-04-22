import datetime

print(datetime.date.today())

dt=datetime.date(1985,1,11)
print(dt)

print(dt.year)
print(dt.month)
print(dt.day)

print(dt.strftime("%d/%m/%Y"))
print(dt.strftime("%a-%m-%y"))
print(dt.strftime("%A-%m-%y"))
print(dt.strftime("%b-%m-%Y"))
print(dt.strftime("%B-%m-%Y"))
print(dt.strftime("%A-%B-%m-%y"))

t=datetime.time(19,56,00)
print(t)

print(t.hour)
print(t.minute)
print(t.second)

print(t.strftime("%I:%M %p"))


print(datetime.datetime.now())
print(dt.strftime("%A %B %d %H:%M"))

