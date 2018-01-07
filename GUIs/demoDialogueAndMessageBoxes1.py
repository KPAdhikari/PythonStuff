'''
Tkinter (and TK of course) provides a set of dialogues (dialogs in American English spelling), which can be used to display message boxes, showing warning or errors, or widgets to select files and colours. There are also simple dialogues, asking the user to enter string, integers or float numbers.

Let's look at a typical GUI Session with Dialogues and Message boxes. There might be a button starting the dialogue, like the "quit" button in the following window:

picture

Pushing the "quit" button raises the Verify window:

picture

Let's assume that we want to warn users that the "quit" functionality is not yet implemented. In this case we can use the warning message to inform the user, if he or she pushes the "yes" button:

picture

If somebody types the "No" button, the "Cancel" message box is raised:

Message box picture

Let's go back to our first Dialogue with the "quit" and "answer" buttons. If the "Answer" functionality is not implemented, it might be useful to use the following error message box:

Python script, which implements the previous dialogue widges:

'''

# For python2
from Tkinter import *
from tkMessageBox import *
# For python3
#from tkinter import *
#from tkinter import messagebox

def answer():
    showerror("Answer", "Sorry, no answer available")

def callback():
    if askyesno('Verify', 'Really quit?'):
        showwarning('Yes', 'Not yet implemented')
    else:
        showinfo('No', 'Quit has been cancelled')

Button(text='Quit', command=callback).pack(fill=X)
Button(text='Answer', command=answer).pack(fill=X)
mainloop()

'''
Message Boxes
The message dialogues are provided by the tkMessageBox module.

The tkMessageBox consists of the following functions, which correspond to dialog windows:

    askokcancel(title=None, message=None, **options)
    Ask if operation should proceed; return true if the answer is ok
    askquestion(title=None, message=None, **options)
    Ask a question
    askretrycancel(title=None, message=None, **options)
    Ask if operation should be retried; return true if the answer is yes
    askyesno(title=None, message=None, **options)
    Ask a question; return true if the answer is yes
    askyesnocancel(title=None, message=None, **options)
    Ask a question; return true if the answer is yes, None if cancelled.
    showerror(title=None, message=None, **options)
    Show an error message
    showinfo(title=None, message=None, **options)
    Show an info message
    showwarning(title=None, message=None, **options)
    Show a warning message
'''
