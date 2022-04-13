# 45

number1 = int(input("Enter a number:\n"))
if number1 <= 50:
    number2 = int(input("Enter a number:\n"))
    total = number1 + number2
    while True:
        if total <= 50:
            number3 = int(input("Enter a number:\n"))
            total += number3
        elif total > 50:
            print("The total is", total)
            break
else:
    print("The total is", number1)

# 46

# while True:
#     user_number = int(input("Enter a number:\n"))
#     if user_number > 5:
#         print("The last number you entered was a", user_number)
#         break

# 47

# number1 = int(input("Enter a number:\n"))
# number2 = int(input("Enter second number:\n"))
# total_2 = number1 + number2
# while True:
#     question = input("Do you want to add another number?\n")
#     if question == "y":
#         another_number = int(input("Enter a number:\n"))
#         total_2 += another_number
#     elif question == "n":
#         print("The total is", total_2)
#         break
#     else:
#         print("I don't understand.\n")
#
