"""
Task -----------------condition------------------------------
Weight converter:
  Input the weight of a person in either kg or lbs. If the person provides his/her
  weight in kg then convert it into lbs
"""
weight = float(input("Enter your weight in kg : "))
kind = input("In which kg or lb you have typed.\n Please 'kg' for kilogram and 'lb' or pound:")
forKg = "kg"
forLb = "lb"
print()
if kind == forKg:
    inLb = weight * 2.20
    print(f"Your weight in pound is {inLb}")
elif kind == forLb:
    inKg = weight / 2.20
    print(f"Your weight in kg is {inKg}")
else:
    print("Invalid typed !")
