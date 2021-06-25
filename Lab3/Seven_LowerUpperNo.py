"""
Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters.
"""


def string(name):
    """
    This module accepts a string and shows total number upper case and lower case used.
    :param name: string
    :return: integer
    """
    upper = 0
    lower = 0
    space = 0
    for i in name:
        a = ord(i)  # ord() gives ASCI
        if a == 32:  # for space
            space += 1
        if a >= 65 and a <= 90:  # 65-90 for Upper case
            upper += 1
        if a >= 97 and a <= 122:  # 97-122 for Lower case
            lower += 1
    total = upper + lower + space
    print(f"Total lower case character is : {lower}")
    print(f"Total upper case character is : {upper}")
    print(f"Total characters in given string is : {total}")


name = "Upper Case Lower Case"
string(name)
