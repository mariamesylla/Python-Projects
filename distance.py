# distance between two points  and draw a triangle

from math import *
from graphics import *

def square(x):
    return x**2


def dist(p1,p2):
    d = sqrt(square(p2.getX()-p1.getX()) + square(p2.getY()-p1.getY()))
    return d


def main():

    win = GraphWin("Draw a triangle")
    win.setCoords(0.0,0.0,10.0,10.0)
    message = Text(Point(5,.5),"Click on three points")
    message.draw(win)

    # clickin in three points
    p1= win.getMouse()
    p1.draw(win)

    p2= win.getMouse()
    p2.draw(win)

    p3= win.getMouse()
    p3.draw(win)

    # drawing a triangle 
    triangle = Polygon(p1,p2,p3)
    triangle.setFill('red')
    triangle.draw(win)

    # Find the perimeter and replace the Text by the perimeter

    perimeter = dist(p1,p2)+dist(p1,p3) + dist(p2,p3)
    message.setText("The perimeter is: {0:0.2f}".format(perimeter))

    win.getMouse()
    win.close



    


main()
