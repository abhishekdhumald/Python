#   Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum.

print("\tEnter any three numbers.")
x1 = int(input("Number 1 : "))
x2 = int(input("Number 2 : "))
x3 = int(input("Number 3 : "))


def fun_sum(x1, x2, x3):
    if x1 == x2 == x3:
        return (print(3 * (x1 + x2 + x3)))
    else:
        return (print(x1 + x2 + x3))


fun_sum(x1, x2, x3)
