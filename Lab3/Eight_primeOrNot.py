# Write a Python function that takes a number as a parameter and check the number is prime or not.
def prime(num):
    """This module inputs a number and checks whether it is prime number or not.
    :param num:
    :return:
    """
    checker = 0
    for i in range(1,num+1):
        if num % i == 0:
            checker += 1
    if checker == 2:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

num = int(input("Enter any positive real number : "))
prime(num)