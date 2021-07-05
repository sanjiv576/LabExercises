# Write a program to find the factorial of a number
product = 1
num = int(input("Input a number : "))
for i in range(1,num+1):
    product *= i
print(f"{num}! = {product}")    