# Write a Python script to sort (ascending and descending) a dictionary by value.

d = {1:'one', 2:'two', 5: 'five', 20: 'twenty', 0:'zero'}
print("In ascending order")
asc = sorted(d)
print(asc)
print("Now, in descending order")
des = asc [::-1]
print(des)

