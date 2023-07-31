# click.py

from graphics import *

def main():
    #Introduction
    #Coordinates of ten successive mouse clicks
    win = GraphWin("Click Me!")
    for i in range(10):
        p = win.getMouse()
        print("You clicked at:", p.getX(), p.getY())
    
main()   
