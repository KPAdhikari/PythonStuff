'''
Indicator
Instead of having radio buttons with circular holes containing white space, we can have radio buttons with the complete text in a box. We can do this by setting the indicatoron (stands for "indicator on") option to 0, which means that there will be no separate radio button indicator. The default is 1.

We exchange the definition of the Radiobutton in the previous example with the following one:
'''


#https://www.python-course.eu/tkinter_radiobuttons.php
#import tkinter as tk
import Tkinter as tk

root = tk.Tk()

#kp: see https://www.python-course.eu/tkinter_variable_classes.php for
#    Variable Classes such as StringVar(), IntVar(), DoubleVar(), BooleanVar().
v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]

def ShowChoice():
    print(v.get())

tk.Label(root,
         text="""Choose your favourite
programming language:""",
         justify = tk.LEFT,
         padx = 20).pack()

for val, language in enumerate(languages):
     tk.Radiobutton(root,
                  text=language,
                  indicatoron = 0,
                  width = 20,
                  padx = 20,
                  variable=v,
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)


root.mainloop()
