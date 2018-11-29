import random
money = 15
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
lose = True
round_ = 1
highscore = 0
best_round = 0
while money > 0:
    print("Round %s" % round_)
    num = 1
    money = money - num
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 + dice2 == 7:
        print("You rolled a 7!")
        print("+ %s, + 4" % num)
        money = money + num
    elif not dice1 + dice2 == 7:
        print("You rolled %s, - %s" % (dice1 + dice2, num))
    if highscore < money:
        highscore = money
        best_round = round_
    print("your new balance is %s" % money)
    round_ = round_ + 1
    print("%s" % round_)
    print("You should have stopped when you had %s in round %s" % (highscore, best_round))
    print()
