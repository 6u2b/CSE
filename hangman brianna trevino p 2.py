import random


word_bank = ["All", "you", "need", "is", "some", "coffee", "and" "some", "good", "music"]

seven = random.choice(word_bank)

List_of_letters = list(seven)
letters_guessed = []
guesses = 8
win = False


while guesses > 0:
    hidden_word = []
    for letter in seven:
        if letter in letters_guessed:
            hidden_word.append(letter)
        else:
            hidden_word.append("*")
    print("".join(hidden_word))

# Take in a guess
    current_guess = input("Type in a letter: ")
    letters_guessed.append(current_guess)

    if current_guess not in seven:
        print("Oops.")
        guesses -= 1

    if "".join(hidden_word) == seven:
            win = True
if win:
    print("You won!")
print("Game end.")
