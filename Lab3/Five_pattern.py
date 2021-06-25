"""
Write a function called show_stars(rows). If rows is 5, it should print the
*
**
***
****
*****
"""


def show_stars(rows):
    for outer in range(rows):
        for inner in range(outer+1):
            print("*", end="")
        print()


show_stars(5)