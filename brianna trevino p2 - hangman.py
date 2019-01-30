import random
import string


word_bank = ["All", "you", "need", "is", "some", "coffee", "and" "some", "good", "music"]

seven = random.choice(word_bank)

List_of_letters = list(seven)
letters_guessed = []
guesses = 8
win = False
hidden_word = []

while guesses > 0 and not win:
    letter = input("put in a letter:")
    for i in range(len(seven)):
        if seven[i] in list(string.punctuation):
            hidden_word.append(seven[i])
        elif seven[i] == "":
            hidden_word.append(seven[i])

        else:
            hidden_word.append("*")
        while guesses > 0:
            hidden_word = []
        for letter in seven:
            if letter in letters_guessed:
                hidden_word.append(letter)
            else:
                hidden_word.append("*")
    print("".join(hidden_word))
    if letter.lower() in letters_guessed:
        print("You already said that.")
    elif letter.lower() in seven.lower():
        print("Yes, that's correct")
        list.append(letters_guessed, letter.lower())
    else:
        print("Nope.")
        list.append(letters_guessed, letter.lower())
        guesses = guesses - 1
