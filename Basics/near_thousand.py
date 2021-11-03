#   Write a Python program to test whether a number is within 100 of 1000 or 2000

def near_thousand(n):
    if abs(1000 - n) <= 100 or abs(2000 - n) <= 100:
        print("\tTrue".format(n))
    else:
        print("\tFalse")


print(near_thousand(1990))
print(near_thousand(957))
