"""
Question No 2
Write a program that reads the length of the base and the height of a
right-angled triangle and prints the area.
Every number is given on a separate line.
"""
base = int(input("Enter the length of the base (in cm) of a right-angled triangle : "))
height = int(input("Enter the height (in cm) of the right-angled triangle : "))
area = (1/2)*base*height
print(f"Area of the right angled triangle is : {area} sq.cm")