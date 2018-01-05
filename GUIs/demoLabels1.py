#https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
#
#from tkinter import *
from Tkinter import *


# creating our class, Window, and inheriting from the Frame class.
#Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
#Then we define the settings upon initialization. This is the master widget.
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
#The above is really all we need to do to get a window instance started.


#Root window created. Here, that would be the only window, but you can later have windows within windows.
root = Tk()

# Now actually creating the instan
app = Window(root)

#Finally, show it and begin the mainloop.
root.mainloop()
#The above code put together should spawn you a window with title 'tk'.
