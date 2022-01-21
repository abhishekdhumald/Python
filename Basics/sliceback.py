letters = "abcdefghijklmnopqrstuvwxyz"
#          01234567890123456789012345
#          65432109876543210987654321
backward = letters[25::-1]
print(backward)

q1 = letters[-10:-13:-1]    # qpo
q2 = letters[4::-1]         # edcba
q3 = letters[:-9:-1]        # Last 8 char in reverse order
print(q1)
print(q2)
print(q3)
print(letters[:len(letters) - 9:-1])        # Last 8 char in reverse order