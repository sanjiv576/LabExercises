# Write a Python program to add member(s) in a set.
s = {3,3,1,5,1,13,34,10}
# s.add(99) # this add an item in the set
s.update([12,31],{44,1111})  # add multiple items
print(s)

# Write a Python program to remove item(s) from set

s.discard(1111)
print(s)