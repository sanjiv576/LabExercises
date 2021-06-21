# Given a positive real number, print its fractional part.

"""
num = int(input("Enter any number : "))
loop = 1
while loop <= num:
    if num % loop == 0:
        print(loop, end=", ")
    loop += 1
"""
import math
num = float(input("Enter any positive real numbers : "))
fractional = math.modf(num)
print(f"Fractional part is {fractional}")


