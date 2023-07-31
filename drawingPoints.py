# drawing points
from graphics import *
def main():
    xList = []
    yList = []
    pointList = []
    fname = input("Enter filename to get the coordinates of points: ")
    infile = open(fname, "r")
    for line in infile:
        x,y=line.split(',')
        xList.append(int(x))
        yList.append(int(y))
        pointList.append(Point(int(x),int(y)))
    infile.close()
        
    win = GraphWin("Scatter plot", 400, 400)
    win.setCoords(-10,-10,max(xList)+10,max(yList)+10)
    win.setBackground("white")
    
    
    for point in pointList:
        C=Circle(point,1)
        C.setFill('red')
        C.draw(win)
    xAxis = Line(Point(-10,0),Point(max(xList),0))
    xAxis.draw(win)
    xLabel= Text(Point(max(xList)+5,-5), 'X')
    xLabel.draw(win)
    yAxis = Line(Point(0,-10),Point(0,max(yList)))
    yAxis.draw(win)
    yLabel= Text(Point(-5,max(yList)+5), 'Y')
    yLabel.draw(win)
                        
       
main()

        
        
