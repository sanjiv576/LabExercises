"""Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20} Expected Result : {0: 10, 1: 20, 2: 30}"""

dictionary = {0: 10, 1: 20}
dictionary[2] = 30
print(dictionary)
dictionary.update({4:40})

print(dictionary)

