# Write a program to find the factorial of a number using functions.
def factorial(num):
    '''
    Only accepts positive integers
    :param num: integer
    :return: integer
    '''
    product = 1
    for i in range(1,num+1):
        product *= i
    return product


num = int(input("Enter any positive integer number : "))
ans = factorial(num)
print(f"The factorial of {num} is {ans}")

print(factorial.__doc__)