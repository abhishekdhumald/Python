
#Write a Python program to accept a filename from the user and print the extension of that.



filename = input("Input the Filename: ")
extns = filename.split(".")
print ("The extension of the file is : " + str(extns[-1]))
