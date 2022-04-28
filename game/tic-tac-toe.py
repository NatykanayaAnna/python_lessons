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


def player_move():
    user_field = None
    click = win.checkMouse()
    if click != None:
        click_x = click.getX()
        click_y = click.getY()
        if 100 <= click_x <= 200 and 100 <= click_y <= 200:
            user_field = 0
    return user_field


def check_fied(avaliable_fields, ch_field):
    for field in avaliable_fields:
        if field == ch_field:
            print("Field avaliable")


avaliable_fields = [0, 1, 2, 3, 4, 5, 6, 7, 8]
field()
text_you()
text_comp()

while True:
    click = player_move()
    if click != None:
        check_fied(avaliable_fields, click)
        break


win.getMouse()