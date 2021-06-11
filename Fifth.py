'''
A school decided to replace the desks in three classrooms.
Each desk sits two students. Given the number of students in each class,
print the smallest possible number of desks that can be purchased.
The program should read three integers:
 the number of students in each of the three classes, a, b and c respectively.
In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.
'''

a = int(input("Enter total number of student in Class 1 : "))
b = int(input("Enter total number of student in Class 2 : "))
c = int(input("Enter total number of students in Class 3 : "))

need1 = a//2
remind1 = a%2
require1 = need1+remind1

need2 = b//2
remind2 = b%2
require2 = need2+remind2

need3 = c//2
remind3 = c%2
require3 = need3+remind3

print(f"Required number of desks in class 1 is : {require1}")
print(f"Required number of desks in class 2 is : {require2}")
print(f"Required number of desks in class 3 is : {require3}")