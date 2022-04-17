# дз из презенташки

# def square():
#     side = int(input("Enter the length of the square side:\n"))
#     perimeter = 4 * side
#     area = side ** 2
#     print("The perimeter of this square is", perimeter)
#     print("The area of this square is", area)
#
#
# square()

# 118

def number():
    num = int(input("Enter a number:\n"))
    return num


def count(num):
    for number in range(1, num + 1):
        print(number)


def main():
    num = number()
    count(num)


main()
