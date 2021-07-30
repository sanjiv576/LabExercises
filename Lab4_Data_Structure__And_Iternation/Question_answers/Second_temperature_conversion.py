""" Write a Python program to convert temperatures to and from celsius,
 fahrenheit.
C = (5/9) * (F - 32)"""
temp = float(input("Input temperature : "))
check = input("In what unit did you provide temperature ? Type 'f' for fahrenheit or 'c' for celsius : ").lower()
if check == 'f':
    celsius = (5/9)*(temp-32)
    print(f"{temp} fahrenheit = {celsius} celsius")
elif check == 'c':
    fahrenheit = ((9/5)*temp)+32
    print(f"{temp} celsius = {fahrenheit} fahrenheit")
else:
    print("Invalid entry !")

