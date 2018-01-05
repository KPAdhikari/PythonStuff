#https://www.python-course.eu/tkinter_radiobuttons.php
#import tkinter as tk
import Tkinter as tk

root = tk.Tk()

#kp: see https://www.python-course.eu/tkinter_variable_classes.php for
#    Variable Classes such as StringVar(), IntVar(), DoubleVar(), BooleanVar().
v = tk.IntVar()

tk.Label(root,
        text="""Choose a
programming language:""",
        justify = tk.LEFT,
        padx = 20).pack()
tk.Radiobutton(root,
              text="Python",
              padx = 20,
              variable=v,
              value=1).pack(anchor=tk.W)
tk.Radiobutton(root,
              text="Perl",
              padx = 20,
              variable=v,
              value=2).pack(anchor=tk.W)

root.mainloop()
