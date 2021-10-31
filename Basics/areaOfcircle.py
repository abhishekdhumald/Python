#   Write a Python program which accepts the radius of a circle from the user and compute the area.

from math import pi

print("Enter the radius of the circle")
radius = float(input("radius = : "))
area = 3.14*(radius**2)
Area = pi*radius**2
print("Area of circle with {0} radius is {1}".format(radius,area))
print("Area of circle with {0} radius is {1}".format(radius,Area))
