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
                  padx = 20,
                  variable=v,
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)


root.mainloop()
