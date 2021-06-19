"""
Task -----------------condition------------------------------
Weight converter:
  Input the weight of a person in either kg or lbs. If the person provides his/her
  weight in kg then convert it into lbs
"""
weight = float(input("Enter your weight : "))
kind = input("In which kg or lb you have typed.\nPlease type 'kg' for kilogram or 'lb' for pound : ").lower()
forKg = "kg"
forLb = "lb"
print()
if kind == forKg:
    inLb = weight * 2.20
    print(f"Your weight in pound is {inLb}")
elif kind == forLb:
    inKg = weight / 2.20
    print(f"Your weight in kilogram is {inKg}")
else:
    print("Invalid typed !")
