import random


def random_word():
    words_list = ["apple", "dog", "flower", "pineapple", "wolf"]
    rand_word = random.choice(words_list)
    return rand_word


def lenght_word(rand_word):
    print(rand_word)
    lenght = len(rand_word)
    count_letters = lenght * ' _ '
    print(count_letters)

guessed_letters = []
word = random_word()
lenght_word(word)
while True:
    guess = input("Enter a letter:\n")
    if guess in word:
        guessed_letters.append(guess)
        print("You guess! The word have this letter\nYou guessed that letters:", guessed_letters)
        word_or_letter = int(input("Enter '1' if you want to guess the word, or '0' for continue guessing the letters:\n"))
        if word_or_letter == 1:
            user_word = input("Enter the word:\n")
            if user_word == word:
                print("This is right! You win!")
                break
            else:
                print("This wrong")
        else:
            continue
    else:
        print("This letter is not in the word")
