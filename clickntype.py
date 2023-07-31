# clickntype.py

from graphics import *

def main():
    #Introduction
    #Get ten keys typed in ten points
    win = GraphWin("Click and Type", 600, 600)
    for i in range(10):
        pt = win.getMouse()
        key = win.getKey()
        label = Text(pt, key)
        label.draw(win)
 
main()   
