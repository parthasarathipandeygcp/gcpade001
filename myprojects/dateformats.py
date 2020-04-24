import datetime

from dateutil.relativedelta import relativedelta

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


delta=datetime.timedelta(days=30)
print(dt + delta)
print(dt - delta)

delta = datetime.timedelta(days= 10, hours=3, minutes=30, seconds=30)
print(dt + delta)


delta=relativedelta(months=1)
print(dt + delta)

delta=relativedelta(years=1)
print(dt + delta)


date1 = datetime.date(2020, 10, 25)
date2 = datetime.date(2019, 12, 25)
diff = date1- date2
print(diff)

months=date1.month - date2.month+12*(date1.year-date2.year)
print(months,'months')




