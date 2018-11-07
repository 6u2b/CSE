import random
print(random. randint(0, 10))
while guesses > 0:
    num = int(input("What's a number from 1 to 10"))
    if num >= 4:
        print("Too high")
        guesses = guesses -1
    elif num <= 2:
        print("a little higher")
    elif num == 3:
        print("Correct")
        guesses = 0

print()
if guesses == 0:
    print("Game over")