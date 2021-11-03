#   Write a Python program to check whether a specified value is contained in a group of values.

def is_value(list, x):
    return x in list


List_1 = [1, 5, 8, 3]
List_2 = [1, 5, 8, 3]

print(is_value(List_1, 3))
print(is_value(List_2, -1))
