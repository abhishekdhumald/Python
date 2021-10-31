#   Python program to display the current date and time.

import datetime

now = datetime.datetime.now()

print("Current Date and Time ")

print(now.strftime("%Y-%M-D    %H:%m:%S"))
