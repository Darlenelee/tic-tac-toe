from graphics import *
import math
def interface():
    global win
    win = GraphWin('tic-tac-toe', 1000, 1000)
    global n
    n = 3
    for i in range(0, n, 1):  # 0,1,2,...n-1
        for j in range(0, n,1):
            r = Rectangle(Point(i*100, (j+1)*100), Point((j+1)*100, 100*i))
            r.draw(win)


def getClick():  # re-orientation x
    click = win.getMouse()
    clickx = click.getX()
    clicky = click.getY()
    x = math.ceil(clickx / 100)
    y = math.ceil(clicky / 100)
    return (x, y)  # 0-14 0-9

def drawCross(x,y):
    line1 = Line(Point(100*x-75, 100*y-75),Point(100*x-25,100*y-25))
    line1.draw(win)
    line2 = Line(Point(100 * x - 75, 100 * y - 25), Point(100 * x - 25, 100 * y - 75))
    line2.draw(win)
def drawCircle(x,y):
    c = Circle(Point(100 * x - 50, 100 * y - 50), 25)
    c.draw(win)

def main():
    interface()
    p1 = getClick()
    drawCross(p1[0], p1[1])
    drawCircle(getClick()[0], getClick()[1])
    getClick()
    win.getMouse()
main()