
# Write a Python program to sum of three given integers. However, if two values are equal, sum will be zero

num1 = int(input("Enter the first integer number : "))
num2 = int(input("Enter the second integer number : "))
num3 = int(input("Enter the third integer number : "))
if num1 == num2 or num1 == num3 or num2 == num3:
   sum = 0
   print(sum)
else:
    sum = num1 + num2 + num3
    print()
    print(f"The sum of {num1},{num2} and {num3} is {sum}")
