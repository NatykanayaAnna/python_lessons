from graphics import *
win = GraphWin('lesson_1', 600, 600)
# vertical
line_1 = Line(Point(200, 100), Point(200, 400))
line_1.draw(win)
line_2 = Line(Point(300, 100), Point(300, 400))
line_2.draw(win)
line_3 = Line(Point(100, 200), Point(400, 200))
line_3.draw(win)
line_4 = Line(Point(100, 300), Point(400, 300))
line_4.draw(win)
win.getMouse()