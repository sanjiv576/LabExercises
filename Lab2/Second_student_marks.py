"""
WAP which accepts marks of four subjects and display total marks, percentage and grade.
Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail
"""
def checker(marks_entry):
    if marks_entry > 100:
        raise ("Wrong entry !. Marks cannot be greater than 100. Rerun again")
    if marks_entry < 0:
        raise ("Wrong entry !. Marks cannot be lesser than 100. Rerun again")

try:
    sub1 = float(input("Enter the marks of the first subject : "))
    marks = sub1
    checker(marks)
    sub2 = float(input("Enter the marks of the second subject : "))
    marks = sub2
    checker(marks)
    sub3 = float(input("Enter the marks of the third subject : "))
    marks = sub3
    checker(marks)
    sub4 = float(input("Enter the marks of the fourth subject : "))
    marks = sub4
    checker(marks)

except ValueError as e:
    print("""
Wrong entry !""")
    print(e)
    print(e.__class__)
    print(e.__class__.__name__)

else:
    totalMarks = sub1+sub2+sub3+sub4
    percentage = (totalMarks/400)*100


    def result():
        print()
        print(f"Your total marks is {totalMarks} out of 400 and percentage is {percentage}% .")
        print()
    if percentage > 70:
        result()
        print("Your grade is distinction.")

    elif percentage > 60:
        result()
        print("Your grade is first division.")
    elif percentage > 40:
        result()
        print("Your grade is pass division.")
    else:
        result()
        print("Your grade is fail.")