# Write a Python program to reverse a string.

def reverse(name):
    """This modules reverses a string."""
    name = input("Enter name : ")[::-1]
    """
    for i in name:
        for j in range(len(name)):
            cat = ''
            j += cat + str(i)
        print(i).reverse()
        """
    print(name)
name = "Anul"
reverse(name)
