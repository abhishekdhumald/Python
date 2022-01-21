
#         43210987654321
# index   01234567890123
parrot = "Norwegian Blue"

'''
print(parrot)
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
print()


print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print()
print(parrot[3 - len(parrot)])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])
print()

print(parrot[0:6])  #Norweg fram index zero to index 6 not six (Exclude 6)
print(parrot[3:5])  #from index 3 to 5(Excluding 5)
print(parrot[0:9])  #from index 0 to 9 (without printing the value at 9)
print(parrot[:9])   #same as above
print(parrot[10:])  #Blue

print(parrot[:])    #   Start at the begining and end at the end

#   print(parrot[AlwaysEnterStartingIndex:EndingIndex])

#   using step in slicing

print(parrot[0:6:2])    # Nre  [ StartingIndex : EndingIndex : Step/Increment]
print(parrot[0:6:3])    # Nw

number = "9,223;372:036;854 775.805"

saparators = number[1::4] # displaying every 4th char
print(saparators)

values = "".join(char if char not in saparators else " " for char in number).split()
print([int(val) for val in values])
print(type(values))

'''

#   Slicing backwords

