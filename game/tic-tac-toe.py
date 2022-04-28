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


field()
text_you()
text_comp()
win.getMouse()