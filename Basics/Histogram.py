#   Write a Python program to create a histogram from a given list of integers.

def histogram(list):
    for n in list:
        output1 = ''
        times = n
        while times > 0:
            output1 = output1 + '*'
            times = times - 1
        print(output1)


List_1 = [1, 2, 7, 3, 7]
List_2 = [4, 6, 3, 9, 2]

histogram(List_1)
print()
histogram(List_2)
