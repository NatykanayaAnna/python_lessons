# def circle():
#     radius = float(input("Enter the radius of the circle:\n"))
#     circle_per = 2 * 3.14 * radius
#     print('Circle perimetr:', circle_per)
#
#
# def square():
#     sq_side = float(input("Enter the side of the square:\n"))
#     sq_per = 4 * sq_side
#     print('Square perimetr:', sq_per)
#
#
# def triangle():
#     tr_side = float(input("Enter the side of the triangle:\n"))
#     tr_per = 3 * tr_side
#     print('Triangle perimetr:\n', tr_per)
#
#
# while True:
#     figure = int(input("Enter:\n1 - Circle\n2 - Square\n3 - Triangle\n0 - Exit\n"))
#     if figure == 1:
#         circle()
#     elif figure == 2:
#         square()
#     elif figure == 3:
#         triangle()
#     elif figure == 0:
#         print("Bye-bye")
#         break
#     else:
#         print("I don't understand")

def circle():
    radius = float(input("Enter the radius of the circle:\n"))
    circle_per = 2 * 3.14 * radius
    return circle_per


def square():
    sq_side = float(input("Enter the side of the square:\n"))
    sq_per = 4 * sq_side
    return sq_per


def triangle():
    tr_side = float(input("Enter the side of the triangle:\n"))
    tr_per = 3 * tr_side
    return tr_per


def main():
    figure_user = int(input("Enter:\n1 - Circle\n2 - Square\n3 - Triangle\n0 - Exit\n"))
    if figure_user == 1:
        circle_menu = circle()
        print(circle_menu)
    elif figure_user == 2:
        square_menu = square()
        print(square_menu)
    elif figure_user == 3:
        triangle_menu = triangle()
        print(triangle_menu)
    elif 3 < figure_user:
        print("I don't underestand.")
    return figure_user


figure = main()
while figure > 0:
    main()
print("Bye_bye")
