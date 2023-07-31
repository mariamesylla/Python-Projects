# poly.py

from graphics import *

def main():
    #Introduction
    #Draw a polygon from mouse clicks
    win = GraphWin("Draw a Polygone")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5,0.5), "Click on five points")
    message.draw(win)
    n = int(input('Enter number of sides: '))

    #Get and draw vertices of polygon
    l = [] #empty list to store points
    for i in range(1,n+1):
        p = win.getMouse()
        l.append(p) # populate your list with the points
        p.draw(win)
    

    #Use Polygon objectto to draw the triangle
    P = Polygon(l) #create your polygone given the list of points
    P.setFill("blue")
    P.setOutline("red")
    P.draw(win)

    #Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()
    
main()  
