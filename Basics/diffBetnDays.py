# Write a Python program to calculate number of days between two dates.


import datetime

f_date = datetime.date(2021, 1, 1)
l_date = datetime.date(2021, 10, 30)
result = l_date - f_date
print(result.days)


today = datetime.date.today()
print(today)

now = datetime.datetime.now()
print(now)
