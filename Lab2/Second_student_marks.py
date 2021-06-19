"""
WAP which accepts marks of four subjects and display total marks, percentage and grade.
Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail
def checker(marks):
    if marks > 100 and marks < 0:
        a = marks
        print("Wrong Entry !")
        return a

"""

sub1 = float(input("Enter the marks of the first subject : "))
sub2 = float(input("Enter the marks of the second subject : "))
sub3 = float(input("Enter the marks of the third subject : "))
sub4 = float(input("Enter the marks of the fourth subject : "))


totalMarks = sub1+sub2+sub3+sub4
percentage = (totalMarks/400)*100
def result():
    print()
    print(f"Your total marks is {totalMarks} and percentage is {percentage}%.")
    print()

if percentage <= 100 and percentage > 70:
    result()
    print("Your grade is distinction.")

elif percentage > 60:
    result()
    print("Your grade is first division.")
elif percentage > 40:
    result()
    print("Your grade is pass division.")
elif percentage >= 0:
    result()
    print("Your grade is fail.")
else:
    print()
    print("Sorry, Invalid entry of subject marks.")
