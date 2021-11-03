#   Write a Python program to count the number 5 in a given list.

def count_5(numbers):
    count = 0
    for num in numbers:
        if num == 5:
            count = count + 1
    return count


List1 = [1,3,6,3,5,8,5,3,5,7,8,5,2]
print(count_5(List1))
List2 = [1, 4, 6, 4, 7, 4]
print(count_5(List2))
