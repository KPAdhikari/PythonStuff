'''
https://www.tutorialspoint.com/python3/tk_messagebox.htm
The tkMessageBox module is used to display message boxes in your applications. This module provides a number of functions that you can use to display an appropriate message.

Some of these functions are showinfo, showwarning, showerror, askquestion, askokcancel, askyesno, and askretryignore.
Syntax

Here is the simple syntax to create this widget −

tkMessageBox.FunctionName(title, message [, options])

Parameters

    FunctionName − This is the name of the appropriate message box function.

    title − This is the text to be displayed in the title bar of a message box.

    message − This is the text to be displayed as a message.

    options − options are alternative choices that you may use to tailor a standard message box. Some of the options that you can use are default and parent. The default option is used to specify the default button, such as ABORT, RETRY, or IGNORE in the message box. The parent option is used to specify the window on top of which the message box is to be displayed.

You could use one of the following functions with dialogue box −

    showinfo()

    showwarning()

    showerror ()

    askquestion()

    askokcancel()

    askyesno ()

    askretrycancel ()

Example

Try the following example yourself −
================


https://stackoverflow.com/questions/16374775/tk-messagebox-import-confusion
tkinter.messagebox is a module, not a class.

import tkinter
tkinter.messagebox  # would raise an ImportError
from tkinter import messagebox
tkinter.messagebox  # now it's available eiter as `messagebox` or `tkinter.messagebox`
'''


# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def hello():
   messagebox.showinfo("Say Hello", "Hello World")

B1 = Button(top, text = "Say Hello", command = hello)
B1.place(x = 35,y = 50)

top.mainloop()
