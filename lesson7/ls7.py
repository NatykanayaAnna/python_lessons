# def number_to_pow(num, pow=2):
#     result = num**pow
#     return result
#
#
# function_result = number_to_pow(2)
# print(function_result)

# def perimeter(*numbers):
#     sum_sides = 0
#     for side in numbers:
#         sum_sides += side
#     print(sum_sides)
#
#
# perimeter(1, 2, 3, 4)

# def subtraction(num1, num2=1):
#     subtraction_numbers = num1 - num2
#     print(subtraction_numbers)
#
#
#
# subtraction(1, 5)

# def message(message_text, count_repet):
#     result = message_text * count_repet
#     print(result)
#
# user_input = input("Enter a message:\n")
# message(count_repet=4, message_text=user_input)

def name():
    user_name = input("Enter your name:\n")
    return user_name


def main():
    user_input = name()
    for letter in user_input:
        print(letter)


main()