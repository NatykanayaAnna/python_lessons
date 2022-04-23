import random


def random_word():
    words_list = ["apple", "dog", "flower", "pineapple", "wolf"]
    rand_word = random.choice(words_list)
    return rand_word


def lenght_word(rand_word):
    lenght = len(rand_word)
    count_letters = lenght * ' _ '
    print(count_letters)
    return lenght


guessed_letters = []
word = random_word()
total_attemps = lenght_word(word) + 1
used_attems = 0
user_word = "0"
while used_attems != total_attemps:
    guess = input("Enter a letter:\n")
    used_attems += 1
    if guess.lower() in word:
        if guess in guessed_letters:
            print("Ты уже угадал эту букву", guessed_letters)
        else:
            guessed_letters.append(guess.lower())
            print("You guess! The word have this letter\nYou guessed that letters:", guessed_letters)
        while True:
            input_word_or_letter = input(
                "Enter '1' if you want to guess the word, or '0' for continue guessing the letters:\n")
            if input_word_or_letter == "1" or input_word_or_letter == "0":
                break
            else:
                print("I don't understand")
        if input_word_or_letter == "1":
            user_word = input("Enter the word:\n")
            if user_word.lower() == word:
                break
            else:
                print("This wrong")
        else:
            continue
    else:
        print("This letter is not in the word")
if user_word.lower() == word:
    print("You win!")
else:
    print("You used all attems. The game is over")
