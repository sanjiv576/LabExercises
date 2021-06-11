"""
Solve each of the following problems using Python Scripts.
Make sure you use appropriate variable names and comments.
 When there is a final answer have Python print it to the screen.
A person’s body mass index (BMI) is defined as:
BMI=mass in kg / (height in m)2.
"""
height = float(input("Enter the height of a person (in m) : "))
mass = float(input("Enter the mass of the person (in kg) : "))
bmi = (mass/height)*2
print(f"A person's body mass index (BMI) is : {bmi}")