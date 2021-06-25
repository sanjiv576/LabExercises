# Write a Python function to find the Max of three numbers.

'''Input three numbers (integer or float).'''


def highestNum(a,b,c):
    '''
    Input numbers can be float or integer, which gives the highest number among them.
    :param a: float or integer
    :param b: float or integer
    :param c: float or integer
    :return: float
    '''
    check = max(a,b,c)
    return check


num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
num3 = float(input("Enter the third number : "))
print(highestNum(num1,num2,num3))
