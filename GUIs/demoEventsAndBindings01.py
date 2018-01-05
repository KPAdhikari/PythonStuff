#http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
'''
In this example, we use the bind method of the frame widget to bind a callback function to an event called <Button-1>. Run this program and click in the window that appears. Each time you click, a message like “clicked at 44 63” is printed to the console window.
'''

from Tkinter import *

root = Tk()

def callback(event):
    print "clicked at", event.x, event.y

frame = Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
