# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements

lst = ['remove1', 20, 30, 'bug', 'remove2', 'remove3', 4.23]
an = lst
for i in an:
    show = an.index(i)
    if show == 0 or show == 4 or show == 5:
        out = lst.pop(show)
    print(i)