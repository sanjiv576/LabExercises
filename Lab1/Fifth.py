'''
A school decided to replace the desks in three classrooms.
Each desk sits two students. Given the number of students in each class,
print the smallest possible number of desks that can be purchased.
The program should read three integers:
 the number of students in each of the three classes, a, b and c respectively.
In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.
'''

student_class1 = int(input("Enter total number of student in the first class  : "))
student_class2 = int(input("Enter total number of student in the second class  : "))
student_class3 = int(input("Enter total number of students in the third class  : "))

need1 = student_class1//2
remind1 = student_class1%2
require1 = need1+remind1

need2 = student_class2//2
remind2 = student_class2%2
require2 = need2+remind2

need3 = student_class3//2
remind3 = student_class3%2
require3 = need3+remind3

total_desks = require1+require2+require3
print()
print(f"Required number of desks in the first class  is : {require1}")
print(f"Required number of desks in the second class  is : {require2}")
print(f"Required number of desks in the third class  is : {require3}")
print()
print(f"Total desks required is : {total_desks}")