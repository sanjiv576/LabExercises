"""
Write a Python program to count the number of even and odd numbers from a
series of numbers.
"""
series = int(input("Give a number upto where you want to know : "))
odd = even = 0
for loop in range(1,series+1):
    print (loop, end=" ")
    if loop % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"""
Number of even numbers is {even}
Number of odd numbers is {odd}""")
