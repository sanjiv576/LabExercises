""" Write a Python program that accepts a string and calculate the number of
 digits and letters"""

string = input("Input a string : ")
letter = digit = 0
for check in string:
    if check.isdigit():
        digit += 1
    elif check.isalpha():
        letter += 1
    else:
        pass

print(f"\nNumber of digits is {digit}")
print(f"Number of letters is {letter}")