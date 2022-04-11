# import random
# right_number = random.randint(1, 10)
# while True:
#     user_number = int(input("guess a number from 1 to 10\n"))
#
#     if user_number == right_number:
#         print("That's right!")
#         break
#     elif user_number > right_number:
#         print("Value is much more than computer value")
#     elif user_number < right_number:
#         print("Value is less than computer value")
# word = input("Write a word:\n")
# for letter in word:
#     print(letter)
numbers = [1, 2, 3, 4, 5, 7, 8, 9]
for letter in numbers:
    print(letter)
right_number = 6
while True:
    user_number = int(input("which number is missed\n"))
    if user_number == right_number:
        print("That is right")
        break
    else:
        print("That is wrong")
