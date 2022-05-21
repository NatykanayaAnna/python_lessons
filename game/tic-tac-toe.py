from graphics import *


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


def text_you(character):
    text = Text(Point(100, 100), 'You:' + character)
    text.draw(win)


def text_comp(character):
    text = Text(Point(400, 100), 'Computer:' + character)
    text.draw(win)


def text_error():
    text = Text(Point(250, 450), 'This field is filled. Choose the another field')
    text.draw(win)


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
            # print(avaliable_fields)


def check_winner(ways_to_win, moves):
    match = 0
    for row in ways_to_win:
        # if row  moves:
        for element in row:
            if element in moves:
                match += 1
                continue
        if match == 3:
            return True
        match = 0
    return False


def user_win_message():
    text = Text(Point(250, 450), 'You won!')
    text.draw(win)


def comp_win_message():
    text = Text(Point(250, 450), 'The computer won!')
    text.draw(win)

def choose_x_o():
    text = Text(Point(300, 200), 'Choose X or O')
    text.setSize(24)
    text.draw(win)


def choose_character():
    click = win.getMouse()
    if click != None:
        click_x = click.getX()
        click_y = click.getY()
        if 305 < click_x < 395 and 230 < click_y < 320:
            return "O"
        if 205 < click_x < 295 and 230 < click_y < 320:
            return "X"


win = GraphWin('lesson_1', 600, 600)
win.setBackground('white')
choose_x_o()
draw_circle((350, 275))
draw_cross((250, 275))
players_character = choose_character()
win.close()
win = GraphWin('lesson_1', 600, 600)
win.setBackground('white')

avaliable_fields = [0, 1, 2, 3, 4, 5, 6, 7, 8]
CENTER_FIELDS = [(150, 150), (250, 150), (350, 150), (150, 250), (250, 250), (350, 250), (150, 350), (250, 350), (350, 350)]
ways_to_win = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
comp_fields = [4, 0, 2, 6, 8, 1, 3, 5, 7]
players_move = []
computers_move = []
field()
text_you(players_character)
if players_character == "X":
    text_comp("O")
    while True:
        click = player_move()
        if click != None:
            center_fields = check_fied(avaliable_fields, click)
            if center_fields:
                draw_cross(center_fields)
                players_move.append(click)
                avaliable_fields.remove(click)
                if len(players_move) >= 3:
                    result = check_winner(ways_to_win, players_move)
                    if result:
                        user_win_message()
                        break
                comp_field = computer_move(comp_fields, avaliable_fields)
                if comp_field:
                    draw_circle(comp_field)
                print(computers_move)
                if len(computers_move) >= 3:
                    result = check_winner(ways_to_win, computers_move)
                    if result:
                        comp_win_message()
                        break
            else:
                text_error()
else:
    click = None
    text_comp("X")
    while True:
        comp_field = computer_move(comp_fields, avaliable_fields)
        print(computers_move)
        if comp_field:
            draw_cross(comp_field)
        if len(computers_move) >= 3:
            result = check_winner(ways_to_win, computers_move)
            if result:
                comp_win_message()
                break
        while True:
            click = player_move()
            if click != None:
                center_fields = check_fied(avaliable_fields, click)
                if center_fields:
                    draw_circle(center_fields)
                    players_move.append(click)
                    avaliable_fields.remove(click)
                    if len(players_move) >= 3:
                        result = check_winner(ways_to_win, players_move)
                        if result:
                            user_win_message()
                            break
                    break
                else:
                    text_error()
                if len(players_move) >= 3:
                    result = check_winner(ways_to_win, players_move)
                    if result:
                        user_win_message()
                        break


win.getMouse()
