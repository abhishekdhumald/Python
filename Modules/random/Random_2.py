#   Write a Python program to select a random element from a list, set, dictionary (value) and a file from a directory.
import random

Colors = ['Green', 'Violet', 'Red', 'Blue', 'Indigo', 'Black', 'White', 'Brown']
print("List Colours contain colors : ", Colors)

print("Random colors from list Colors are : ")

print(random.choice(Colors))
print(random.choice(Colors))
print(random.choice(Colors))


elements = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 12])
print("\nSelect a random element from a set: ", elements)
# converting to tuple because sets are invalid inputs
print(random.choice(tuple(elements)))
print(random.choice(tuple(elements)))
print(random.choice(tuple(elements)))

d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print("\nSelect a random value from a dictionary: ", d)
print("\tPrinting in key-value pair.")

key = random.choice(list(d))
print(key, ":", d[key])

key = random.choice(list(d))
print(key, ":", d[key])

key = random.choice(list(d))
print(key, ":", d[key])


print("\nSelect a random file from a directory.:")
print(random.choice(os.listdir("/")))

