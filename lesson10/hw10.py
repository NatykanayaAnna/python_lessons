# номер 88


nums = [4, 10, 20, 2, 1]        # я не знаю, как правильно попросить пользователя ввести список, поэтому сделала свой
nums = sorted(nums)
nums.reverse()
print(nums)


# номер 93


# numbers = []
# removed_nums = []
# len_list = 0
# while len_list < 4:
#     len_list = len(numbers)
#     user_num = int(input("Enter the number:\n"))
#     numbers.append(user_num)
# numbers = sorted(numbers)
# selected_number = int(input("Select the number:\n"))
# numbers.remove(selected_number)
# removed_nums.append(selected_number)


# номер 94


# nums = [4, 7, 6, 30, 10]
# print(nums)
# while True:
#     selected_num = int(input("Select the number:\n"))
#     if selected_num not in nums:                          # можно ли использовать not in?
#         print("Try again.")
#     else:
#         print("Position of that number is", nums.index(selected_num))
#         break
