# Write a Python program to unpack a tuple in several variables.
tup = (4,12,4,2,-1,'abc', 'heat', 2.23)
(a,b,c,d,e,f,*g) = tup
print(a,b,c,d,e,f,g)