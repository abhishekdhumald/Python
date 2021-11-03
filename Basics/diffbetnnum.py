#   Write a Python program to get the difference between a given number and 17,
#   if the number is greater than 17 return double the absolute difference.

x = int(input("\tEnter any Number : "))

def given_fun(x):
    if x <= 17:
        return(17-x)
    else:
        return(2*(x-17))


print(given_fun(x))
