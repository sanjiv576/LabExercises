# Write a Python function that checks whether a passed string is palindrome or not.

def palindrome(string):
    '''
    Input is string. Checks whether it is palindrome string or not.
    :param string: string
    :return: string
    '''
    checker = string
    reverseString = string[::-1]
    if reverseString == checker:
        print(f"{checker} is a palindrome string")
    else:
        print(f"{checker} is not a palindrome string")


string = input("Enter a string in lowercase : ").lower()
palindrome(string)