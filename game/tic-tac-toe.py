from graphics import *
import timeit


def field():
    # vertical
    line_1 = Line(Point(200, 100), Point(200, 400))
    line_1.setWidth(3)
    line_1.draw(win)
    line_2 = Line(Point(300, 100), Point(300, 400))
    line_2.setWidth(3)
    line_2.draw(win)
    line_3 = Line(Point(100, 200), Point(400, 200))
    line_3.setWidth(3)
    line_3.draw(win)
    line_4 = Line(Point(100, 300), Point(400, 300))
    line_4.setWidth(3)
    line_4.draw(win)


def text_message(coordinates,  msg, text_size=10):
    text = Text(Point(coordinates[0], coordinates[1]), msg)
    text.setSize(text_size)
    text.draw(win)
    return text


def player_move():
    user_field = None
    click = win.checkMouse()
    if click != None:
        click_x = click.getX()
        click_y = click.getY()
        if 100 <= click_x <= 200 and 100 <= click_y <= 200:
            user_field = 0
        elif 200 <= click_x <= 300 and 100 <= click_y <= 200:
            user_field = 1
        elif 300 <= click_x <= 400 and 100 <= click_y <= 200:
            user_field = 2
        elif 100 <= click_x <= 200 and 200 <= click_y <= 300:
            user_field = 3
        elif 200 <= click_x <= 300 and 200 <= click_y <= 300:
            user_field = 4
        elif 300 <= click_x <= 400 and 200 <= click_y <= 300:
            user_field = 5
        elif 100 <= click_x <= 200 and 300 <= click_y <= 400:
            user_field = 6
        elif 200 <= click_x <= 300 and 300 <= click_y <= 400:
            user_field = 7
        elif 300 <= click_x <= 400 and 300 <= click_y <= 400:
            user_field = 8
        # print(user_field)
    return user_field


def check_fied(avaliable_fields, checking_field):
    if checking_field in avaliable_fields:
        return CENTER_FIELDS[checking_field]
    return False


def draw_cross(center):
    line_1 = Line(Point(center[0] - 45, center[1]-45), Point(center[0] + 45, center[1] + 45))
    line_1.setWidth(3)
    line_1.setOutline("green")
    line_1.draw(win)
    line_2 = Line(Point(center[0] + 45, center[1] - 45), Point(center[0] - 45, center[1] + 45))
    line_2.setWidth(3)
    line_2.setOutline("green")
    line_2.draw(win)


def draw_circle(center):
    circle = Circle(Point(center[0], center[1]), 45)
    circle.setWidth(3)
    circle.setOutline("red")
    circle.draw(win)


def computer_move(comp_fields, avaliable_fields):
    for field in comp_fields:
        if field in avaliable_fields:
            comp_fields.remove(field)
            avaliable_fields.remove(field)
            computers_move.append(field)
            return CENTER_FIELDS[field]


# def check_winner(ways_to_win, moves):
#     match = 0
#     for row in ways_to_win:
#         for element in row:
#             if element in moves:
#                 match += 1
#                 continue
#         if match == 3:
#             return True
#         match = 0
#     return False
def check_winner(ways_to_win, moves):
    for row in ways_to_win:
        if len(set(row) & set(moves)) == 3:
            return True
    return False


def choose_character():
    click = win.getMouse()
    if click != None:
        click_x = click.getX()
        click_y = click.getY()
        if 305 < click_x < 395 and 230 < click_y < 320:
            return "O"
        if 205 < click_x < 295 and 230 < click_y < 320:
            return "X"


def check_win(moves_list, ways_to_win):
    if len(players_move) >= 3:
        start = timeit.default_timer()
        # Your statements here
        returned = check_winner(ways_to_win, moves_list)
        stop = timeit.default_timer()
        print('Time: ', stop - start)
        returned = check_winner(ways_to_win, moves_list)
        return returned
    return False


win = GraphWin('tic-tac-toe', 600, 600)
win.setBackground('white')
text_message((300, 200), 'Choose X or O', 24)
draw_circle((350, 275))
draw_cross((250, 275))
players_character = choose_character()
win.close()
win = GraphWin('tic-tac-toe', 600, 600)
win.setBackground('white')

avaliable_fields = [0, 1, 2, 3, 4, 5, 6, 7, 8]
CENTER_FIELDS = [(150, 150), (250, 150), (350, 150), (150, 250), (250, 250), (350, 250), (150, 350), (250, 350), (350, 350)]
ways_to_win = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
comp_fields = [4, 0, 2, 6, 8, 1, 3, 5, 7]
players_move = []
computers_move = []
field()
text = text_message((100, 100), 'You:' + players_character)
if players_character == "X":
    text = text_message((400, 100), 'Computer: O')
    while True:
        click = player_move()
        if click != None:
            center_fields = check_fied(avaliable_fields, click)
            if center_fields:
                draw_cross(center_fields)
                players_move.append(click)
                avaliable_fields.remove(click)
                if check_win(players_move, ways_to_win):
                    text.undraw()
                    text = text_message((250, 450), 'You won!')
                    break
                comp_field = computer_move(comp_fields, avaliable_fields)
                if comp_field:
                    draw_circle(comp_field)
                if check_win(computers_move, ways_to_win):
                    text.undraw()
                    text = text_message((250, 450), 'The computer won!')
                    break
                result = check_winner(ways_to_win, computers_move)
                if len(avaliable_fields) == 0 and result == False:
                    text.undraw()
                    text = text_message((250, 450), 'Draw!')
                    break
            else:
                text = text_message((250, 450), 'This field is filled. Choose the another field')
else:
    click = None
    text = text_message((400, 100), 'Computer: X')
    while True:
        comp_field = computer_move(comp_fields, avaliable_fields)
        if comp_field:
            draw_cross(comp_field)
        if check_win(players_move, ways_to_win):
            text.undraw()
            text = text_message((250, 450), 'You won!')
            break
        if check_win(computers_move, ways_to_win):
            text.undraw()
            text = text_message((250, 450), 'The computer won!')
            break
        result = check_winner(ways_to_win, computers_move)
        if len(avaliable_fields) == 0 and result == False:
            text.undraw()
            text = text_message((250, 450), 'Draw!')
            break
        while True:
            click = player_move()
            if click != None:
                center_fields = check_fied(avaliable_fields, click)
                if center_fields:
                    draw_circle(center_fields)
                    players_move.append(click)
                    avaliable_fields.remove(click)
                    if check_win(players_move, ways_to_win):
                        text.undraw()
                        text = text_message((250, 450), 'You won!')
                        break
                    break
                else:
                    text.undraw()
                    text = text_message((250, 450), 'This field is filled. Choose the another field')
                # if check_win(players_move, ways_to_win):
                #         text_message((250, 450), 'You won!')
                #         break
win.getMouse()
# Time:  4.499999704421498e-06
# Time:  3.300001480965875e-06
# Time:  3.399998604436405e-06

# Time:  4.499999704421498e-06
# Time:  3.4000004234258085e-06
# Time:  3.0000010156072676e-06