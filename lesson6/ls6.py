# def season(month):
#     if month <= 2 or month == 12:
#         print("Winter")
#     elif month >=3 and month <= 5:
#         print("Sprint")
#     elif month >=6 and month <=8:
#         print("Summer")
#     elif month >= 9 and month <= 11:
#         print("Autumn")
#
#
# season(int(input("Enter a number of month:\n")))
#область создания функций
# def counter():
#     num=int(input('Введите число \n'))
#     for i in range(num+1):
#         print(i)
#         return i
# #область вызова функций
# while True:
#     num_from_function = counter()
#     print(num_from_function)

import random

def num(low, high):
    comp_num = random.randint(low, high)
    return comp_num


def guess():
    guess_num = int(input("Guess the number"))
    return guess_num


def guess_number(guess_num, comp_num):
    if guess_num == comp_num:
        print("You're right")

    else:
        print("This is wrong")

def main():
    comp_main = num(4, 9)
    print(comp_main)
    guess_main = guess()
    print(guess_main)
    guess_number(comp_main, guess_main)


main()
# print(num(4, 8))