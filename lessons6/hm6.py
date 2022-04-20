def circle():
    radius = float(input("Enter the radius of the circle:\n"))
    circle_per = 2 * 3.14 * radius
    print('Circle perimetr:', circle_per)


def square():
    sq_side = float(input("Enter the side of the square:\n"))
    sq_per = 4 * sq_side
    print('Square perimetr:', sq_per)


def triangle():
    tr_side = float(input("Enter the side of the triangle:\n"))
    tr_per = 3 * tr_side
    print('Triangle perimetr:\n', tr_per)


while True:
    figure = int(input("Enter:\n1 - Circle\n2 - Square\n3 - Triangle\n0 - Exit\n"))
    if figure == 1:
        circle()
    elif figure == 2:
        square()
    elif figure == 3:
        triangle()
    elif figure == 0:
        print("Bye-bye")
        break
    else:
        print("I don't understand")
