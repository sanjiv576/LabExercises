"""
8. Write a Python program which accepts the radius of a circle from the user and compute the area.
(area of circle = PI * r2)
"""

radius = float(input("Enter the radius of a circle (in cm) : "))
pi = 3.14
area = pi*radius**2
print("Area of the circle is : %f sq.cm" % area)
