import random
money = 15
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
lose = True
while money > 0:
    num = 1
    money = money - num
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 + dice2 == 7:
        print("You rolled a 7!")
        print("your new balance is %s" % money)
        print("+ %s, + 4" % num)
    elif not dice1 + dice2 == 7:
        print("You got %s and %s, - %s" % (dice1, dice2, num))
