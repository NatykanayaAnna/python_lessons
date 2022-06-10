#ex.1
user_word = input("Enter a word:\n")
user_word_par = ''.join(reversed(user_word))
if user_word == user_word_par:
    print("That word is palindrome")
else:
    print("That word isn't palindrome")
#ex.2
# list = [-4, 5, 10, -23, -1]
# print(list)
# negative_num = []
# positive_num = []
# for num in list:
#     if num < 0:
#         negative_num.append(num)
#     elif num > 0:
#         positive_num.append(num)
# print(negative_num)
# print(positive_num)