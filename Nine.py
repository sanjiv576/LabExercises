"""
Write a python program to find sum of the first n positive integers.
sum = (n*(n+1))/2

Without formula :

startNum = int(input("Enter the number that starts with : "))
endNum = int(input("Enter the number that ends with : "))
n = int(input("Enter a number to find sum of the first n numbers : "))
sum = 0
counter = 0
print()
for i in range(startNum, endNum+1, 1):
    counter += 1
    if counter == n+1: # +1 is added in n to control flow upto n and then, terminating the program
        print(f"Sum of the first {n} from given series is : {sum}")
        break
    sum += i
"""
firstNo = int(input("Enter a number to find sum of the first n number : "))
sum = (firstNo*(firstNo+1))*0.5
print(f"Sum of the first {firstNo} number is : {sum}")

