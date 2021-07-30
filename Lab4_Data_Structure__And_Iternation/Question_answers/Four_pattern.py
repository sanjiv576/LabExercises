"""
Write a Python program to construct the following pattern, using a nested for loop.
*
**
***
****
*****
****
***
**
*

"""
for rows1 in range(1,6):
    for column_increment in range(1,rows1+1):
        print("*", end=" ")
    print()

for rows2 in range(4,0,-1):
    for column_decrement in range(1,rows2+1):
        print("*", end=" ")
    print()

"""loop = 0
for row in range(1,10):
    for column_increment in range(row):
        if row >= 6:
            loop += 1
            for column_decrement in range(4,1,-1):
                print("*", end=" ")
            print()   
        else:
             print("*", end=" ")
    if row <= 5:
        print()"""
