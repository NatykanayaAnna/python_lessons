# first_number = int(input("Enter a number over 100:\n"))
# if first_number <= 100:
#     print("This number isn't over 100")
# second_number = int(input("Enter a number under 10:\n"))
# if second_number >= 10:
#     print("This number isn't under 10")
# difference_numbers = first_number/second_number
# print(difference_numbers, "times the smallest number does into the largest number")
# favourite_color = input("Enter your favourite color:\n")
# if favourite_color == "red":
#     print("I like red too")
# elif favourite_color == "RED":
#     print("I like red too")
# elif favourite_color == "Red":
#     print("I like red too")
# else:
#     print("I don’t like {}, I prefer red".format(favourite_color))
# favourite_color = input("Enter your favourite color:\n")
# if favourite_color == "red" or favourite_color == "RED" or favourite_color == "Red":
#     print("I like red too")
# else:
#     print("I don’t like {}, I prefer red".format(favourite_color))
# favourite_color = input("Enter your favourite color:\n")
# if favourite_color.lower() == "red":
#     print("I like red too")
# else:
#     print("I don’t like {}, I prefer red".format(favourite_color))
direction = input("Which direction you want to count(up or down)?\n")
if direction == "up":
    number_up = int(input("Enter the top number:\n"))
    for number in range(1, number_up):
        print(number)
elif direction == "down":
    number_down = int(input("Enter a number below 20:\n"))
    for number in range(20, number_down, -1):
        print(number)
else:
    print("I don't understand")