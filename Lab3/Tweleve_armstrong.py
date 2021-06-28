"""Write a python program to check whether the number is Armstrong number or not using function:
[Hint: 153 - 1*1*1 + 5*5*5 + 3*3*3]
"""
def armstrong():
    num = int(input("Enter a number : "))
    result = 0
    original = num
    for i in range(3):
        remainder = num % 10
        result = (remainder**3)+result
        num //= 10
    print(result)
    if result == original:
        print(f"{original} is an armstrong number.")
    else:
        print(f"{original} is not an armstrong number")


armstrong()