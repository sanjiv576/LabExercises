"""
game finding a secret number within 3 attempts using while loop


import random
randomNum = random.randint(1, 3)
guessNum = int(input("Guess number from 1 to 10 : "))
attempt = 1
while attempt <= 2:
    if guessNum == randomNum:
        print("Congratulations! You have have found the secret number.")
        break
    else:
        again = int(input("Guess again : "))
    attempt += 1
else:
    print("Sorry ! You have crossed the limitation.")
"""
import random
randomNo = random.randint(0, 2)
guessNo = int(input('Guess a number from 0 to 9 : '))
attempt = 1
while randomNo != guessNo:
    if attempt <= 2:
        guessNo = int(input('Guess again : '))
    else:
        print("Sorry ! you've reached your limitation.")
        break
    attempt += 1
if guessNo == randomNo:
    print("Congratulations! You've found the secret number.")

