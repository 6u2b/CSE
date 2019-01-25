import random
import string


word_bank = ["All", "you", "need", "is", "some", "coffee", "and" "some", "good", "music"]

seven = random.choice(word_bank)

List_of_letters = list(seven)
letters_guessed = []
guesses = 8
win = False
blank = []

for i in range(len(seven)):
    if seven[i] in list(string.punctuation):
        blank.append(seven[i])
    elif seven[i] == "":
        blank.append(seven[i])
    elif seven[i] == "":
        blank.append("")
    else:
        blank.append("*")
    while guesses > 0:
        hidden_word = []
    for letter in seven:
        if letter in letters_guessed:
            blank.append(letter)
        else:
            blank.append("*")
print("".join(blank))

while guesses > 0 and not win:
    letter = input("put in a letter")
    if letter.lower() in letters_guessed:
        print("You already said that.")
    elif letter.lower() in seven.lower():
        print("Yes, that's correct")
        list.append(letters_guessed, letter.lower())
    else:
        print("Nope.")
        list.append(letters_guessed, letter.lower())
        guesses = guesses - 1
