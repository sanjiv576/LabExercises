# Write a Python program to iterate over dictionaries using for loops.

d = {'cat': 20, 'hat': 30, 'fat': 3}
for i in d:
    print(i)

print("---------------------------------")
# Write a Python program to sum all the items in a dictionary.

dictionary = {9: 1, 10: 10, 11: 12, 12: 1, 13: 6, 14: 2, 15: 6}
add = dictionary.values()  # values() returns values of the dictionary
print(sum(add))  # sum() directly adds the values of the dictionary
