from graphics import *
import math

win = GraphWin('Graph of a logistic model',width=700,height=700)

r = 0.025
L = 200

for t in range(0,200,10):
    P = Point(t,200- L/(1 + 24*math.e**(-r*t)))
    print(t, 200- L/(1 + 24*math.e**(-r*t)))
    P.draw(win)
