name = input("Enter your name : ")
age = int(input("Enter your age : "))
print("Hello, my name is " + name + " and I am " + str(age) + " years old.")
print("Hello, my name is ", name, " and I am ", age, " years old.")
print("Hello, my name is %s and i am %d years old" % (name, age))
print("Hello, my name is {} and i am {} years old".format(name, age))
print(f"Hello, my name is {name} and i am {age} years old.")
