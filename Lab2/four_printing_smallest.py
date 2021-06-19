"""
Question 4
Given three integers, print the smallest one. (Three integers should be user input)
"""
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))
if num1 < num2 and num1 < num3:
    print(f"{num1} is the smallest number among {num2} and {num3}")
elif num2 < num1 and num2 < num3:
    print(f"{num2} is the smallest number among {num1} and {num3}")
else:
    print(f"{num3} is the smallest number among {num1} and {num2}")

