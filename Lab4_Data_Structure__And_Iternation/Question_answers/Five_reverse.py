# Write a Python program that accepts a word from the user and reverse it.

string = input("Give a string : ")
reversed = string [::-1]
print(reversed)


def reversed(string):

    reversing = ''
    length = len(string)
    while length > 0:
        reversing += string[length-1]
        length -= 1
    print(reversing)


string = input("Enter a string : ")
reversed(string)
