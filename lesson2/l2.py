# people = int(input("Сколько людей?\n"))
# pizza = float(input("Сколько пиццы?\n"))
# result = pizza/people
# print(result, "столько кусочков на человека.")
# password = 1234
#
# while True:
#     password_user = int(input("Введите пароль\n"))
#     if password == password_user:
#         print("Открыть дверцу сейфа")
#         break
#     else:
#         print("Пароль не правильный!")
#
# print("Птица, которая носит костюм - это...")
# right_word = "пингвин"
# while True:
#     user_word = input()
#     if user_word == right_word:
#         print("Да! Все верно!")
#         break
#     else:
#         print("НЕ верно!")
while True:
    user_number = int(input("guess a number from 1 to 10\n"))
    right_number = 7
    if user_number == right_number:
        print("That's right!")
        break
    else:
        print("That's wrong. Try again!")