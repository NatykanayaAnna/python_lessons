from graphics import *

win = GraphWin('lesson_1', 600, 600)
win.setBackground('white')


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


def text_you():
    text = Text(Point(100, 100), 'You: X')
    text.draw(win)


def text_comp():
    text = Text(Point(400, 100), 'Computer: O')
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
    line_1 = Line(Point(center[0] - 50, center[1]-50), Point(center[0] + 50, center[1] + 50))
    line_1.setWidth(3)
    line_1.draw(win)
    line_2 = Line(Point(center[0] + 50, center[1] - 50), Point(center[0] - 50, center[1] + 50))
    line_2.setWidth(3)
    line_2.draw(win)


def computer_move(comp_fields, avaliable_fields):
    for fields in comp_fields:
        if fields in avaliable_fields:
            pass
            # draw circle



avaliable_fields = [0, 1, 2, 3, 4, 5, 6, 7, 8]
CENTER_FIELDS = [(150, 150), (250, 150), (350, 150), (150, 250), (250, 250), (350, 250), (150, 350), (250, 350), (350, 350)]
comp_fields = [4, 0, 2, 6, 8, 1, 3, 5, 7]
field()
text_you()
text_comp()

while True:
    click = player_move()
    if click != None:
        center_fields = check_fied(avaliable_fields, click)
        if center_fields:
            draw_cross(center_fields)
            avaliable_fields.pop(click)
        else:
            text_error()
        # break


win.getMouse()
