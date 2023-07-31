# triangle.py

from graphics import *

def main():
    #Introduction
    #Draw a triangle given three mouse clicks
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5,0.5), "Click on three points")
    message.draw(win)

    #Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    #Use Polygon objectto to draw the triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("green")
    triangle.setOutline("red")
    triangle.draw(win)

    #Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()
    
main()   
