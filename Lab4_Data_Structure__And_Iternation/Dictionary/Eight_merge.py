"""Write a Python script to merge two Python dictionaries."""
d = {1: 10, 2: 20}
d2 = {'one': 1, 'two': 2}
merging = {**d, **d2}
print(merging)