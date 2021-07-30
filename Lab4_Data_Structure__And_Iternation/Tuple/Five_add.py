# Write a Python program to add an item in a tuple.

tup = (10, 20, 30, 40, 'code')
lst = list(tup)
lst.insert(2,'added item')
newTuple = tuple(lst)  # conversion list into tuple
print(newTuple)

