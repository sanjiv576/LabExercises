# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements

lst = ['remove1', 20, 30, 'bug', 'remove2', 'remove3', 4.23]
new_list = []
for i in lst:

    if i != lst[0] and i != lst[4] and i != lst[5]:
        new_list.append(i)


print(new_list)
