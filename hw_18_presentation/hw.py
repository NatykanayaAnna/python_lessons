import random


def user_input():
    text = input("Enter your string:\n")
    return text


def caps_text(text):
    text = text.upper()
    return text


def sort_text(upper_text):
    vowels = {"E", "Y" "U", "I", "O", "A"}
    vow_let = []
    con_let = []
    letters = set(upper_text)
    con_let = letters - vowels
    if len(vow_let) > len(con_let):
        return list(vow_let)
    else:
        return list(con_let)


def rand_letter(letters):
    letter = random.choice(letters)
    print(letter)


user_text = user_input()
caps = caps_text(user_text)
print(caps)
sorted_text = sort_text(caps)
letter = rand_letter(sorted_text)
