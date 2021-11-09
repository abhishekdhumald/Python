#   Write a Python program to generate
#   a random alphabetical character,
#   alphabetical string and
#   alphabetical string of a fixed length.

import random
import string

#   a random alphabetical character,
a = 0
while a < 5:
    print("A random alphabetical character is : ", random.choice(string.ascii_letters))
    a = a + 1

#   alphabetical string
a = 0
max_len = 150
while a < 5:
    alphabetical_string = ''
    for x in range(1, random.randint(1, max_len)):
        alphabetical_string = alphabetical_string + random.choice(string.ascii_letters)
    print("Alphabetical string is : ", alphabetical_string)
    a = a + 1

#   alphabetical string of a fixed length.
a = 0
while a < 5:
    alphabetical_string = ''
    for x in range(10):
        alphabetical_string = alphabetical_string + random.choice(string.ascii_letters)
    print("Alphabetical string of fixed length is : ", alphabetical_string)
    a = a + 1
