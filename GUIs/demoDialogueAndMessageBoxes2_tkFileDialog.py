'''
https://www.python-course.eu/tkinter_dialogs.php
Open File Dialogue
There is hardly any serious application, which doesn't need a way to read from a file or write to a file. Furthermore, such an application might have to choose a directory. Tkinter provides the module tkFileDialog for these purposes.
'''

from Tkinter import *
from tkFileDialog   import askopenfilename

def callback():
    name= askopenfilename()
    print name # kp: name will have the full path of the file selected

errmsg = 'Error!'
#kp: raise err(errmsg)
Button(text='File Open', command=callback).pack(fill=X)
mainloop()


'''
The code above creates a window with a single button with the text "File Open". If the button is pushed, the following window appears:

Choosing a file

The look-and-feel of the file-open-dialog depends on the GUI of the operating system. The above example was created using a gnome desktop under Linux. If we start the same program under Windows 7, it looks like this:

Choosing a file the Windows 7 way
'''
