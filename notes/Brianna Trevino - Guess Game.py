import random

number = random.randint(1, 10)
guesses = 5
while guesses > 0:
    num = int(input("What's a number from 1 to 10"))
    if num > number:
        print("Too high")
        guesses = guesses -1
    elif num < number:
        print("a little higher")
    elif num == number:
        print("Correct")
        guesses = 0

print()
if guesses == 0:
    print("Game over")