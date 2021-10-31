#   Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them

print("Enter your name")
FirstName = input("First Name : ")
LastName = input("Last Name : ")

print("{0} {1} is your name".format(FirstName,LastName))

print("{0} {1} is your name in reverse".format(LastName,FirstName))
