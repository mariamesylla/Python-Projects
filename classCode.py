'''from tkinter import *

class Window(Frame):

    def init (self , master = None):
        Frame.init(self , master)
        self.master = master
root = Tk()


#app = Window(root)
w=Label(root, text="Hello, world")
w.pack()
root.mainloop()
'''
from graphics import *




win = GraphWin('A window with shapes') #What do things inside
center1 = Point(60,80) #What is this?
circ1 = Circle(center1 , 20) #What is this?
circ1.draw(win) #What will this do?
center1.draw(win) #What does this do?
center2 = Point (120 , 150)
circ2 = Circle(center2 , 30)
circ2.setFill('Blue')
circ2.draw(win)
label1 = Text(center1 , "White circle ")
label2 = Text(center2 , "Blue circle ")
label1.draw(win)
label2.draw(win)
win.getMouse()
win.close( )


