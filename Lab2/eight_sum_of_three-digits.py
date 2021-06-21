"""
Given a three-digit number. Find the sum of its digits.
10.
"""
num = int(input("Enter any three-digits number : "))
copidNum = num
sum = 0
for i in range(3):
    remainder = copidNum % 10
    sum += remainder
    copidNum //= 10
print(f"Sum of each digit of {num} is {sum}")