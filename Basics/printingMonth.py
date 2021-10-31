#   Write a Python program to print the calendar of a given month and year.

import calendar

m = int(input("Enter Month number: "))
y = int(input("Enter year : "))

print(calendar.month(y,m))
