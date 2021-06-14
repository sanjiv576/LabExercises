"""
 If temperature is greater than 30, it's a hot day other wise if it's less than 10;
 it's a cold day; otherwise, it's neither hot nor cold.
"""
temp = float(input("Enter the temperature : "))
if temp > 30:
    print("It's s hot day ")
elif temp < 10:
    print("It is a cold day")
else:
    print("It is neither hot nor cold")