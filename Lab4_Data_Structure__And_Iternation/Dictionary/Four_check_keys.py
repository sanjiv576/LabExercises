# Write a Python script to check if a given key already exists in a dictionary.
dic1 = {1: 'one', 2: 'two', 3: 'three'}
keyOnly = dic1.keys()
check = int(input("Input a key : "))
if check in keyOnly:
    print(f"{check} key already exists.")
else:
    print(f"{check} key is not in {dic1}")
