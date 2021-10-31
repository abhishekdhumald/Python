#   Write a Python program which accepts a sequence of comma-separated numbers from user and
#   generate a list and a tuple with those numbers

values = input("Enter some coma separated numbers :")

list = values.split(",")

print(list)
print(tuple(list))
