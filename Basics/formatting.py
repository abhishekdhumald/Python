for i in range(1, 13):
    print("No. {0:2} squared {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))  # {x:y}  { x is value : y is number of fields reserved for x on output screen }
    print("No. {0:<2} squared {1:>4} and cubed is {2:^4}".format(i, i ** 2, i ** 3))  # (<:left allign)(>:right allign)(^:center allign)

print()

print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:<72.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))

for i in range(1, 13):
    print("No. {} squared {} and cubed is {:4}".format(i, i ** 2, i ** 3)) # if we specify number inside {} we can reuse and change the order of it

