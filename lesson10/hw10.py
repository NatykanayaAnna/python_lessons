# exercise 88


user_list = []
user_string = input('Input list use comma')
user_list= list(user_string)
user_list = sorted(user_list)
user_list.reverse()
print(user_list)


# ex.93


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


# ex. 94


# nums = [4, 7, 6, 30, 10]
# print(nums)
# while True:
#     selected_num = int(input("Select the number:\n"))
#     if selected_num not in nums:
#         print("Try again.")
#     else:
#         print("Position of that number is", nums.index(selected_num))
#         break
