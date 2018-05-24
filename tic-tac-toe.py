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

'''
    789  1,1 2,1 3,1
    456  1,2 2,2 3,2
    123  1,3 2,3 3,3
'''
def getClick():  # re-orientation
    click = win.getMouse()
    clickx = click.getX()
    clicky = click.getY()
    x = math.ceil(clickx / 100)
    y = math.ceil(clicky / 100)
    print (x,y)
    return (x + 3 * (3-y))


def drawCross(x,y):
    # type: (object, object) -> object
    line1 = Line(Point(100*x-75, 100*y-75),Point(100*x-25,100*y-25))
    line1.draw(win)
    line2 = Line(Point(100 * x - 75, 100 * y - 25), Point(100 * x - 25, 100 * y - 75))
    line2.draw(win)
def drawCircle(x,y):
    c = Circle(Point(100 * x - 50, 100 * y - 50), 25)
    c.draw(win)

def main():
    interface()
    board = [' ']*10
    while(True):
        p1 = getClick()
        drawCross(p1[0], p1[1])
        p2 = getClick()
        drawCircle(p2[0], p2[1])
        getClick()
    win.getMouse()
main()