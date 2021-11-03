#   Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def mul_str(str, n):
    result = ""
    for i in range(n):
        result = result + str
    return (result)


print(mul_str('abc', 8))
print(mul_str('.py', 5))
