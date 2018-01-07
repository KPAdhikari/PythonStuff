'''
https://www.python-course.eu/tkinter_layout_management.php

Introduction
Packed Suitcases, from Wikipedia, Public Domain, Sherlock_Holmes_Museum In this chapter of our Python-Tkinter tutorial we will introduce the layout managers or geometry managers, as they are sometimes called as well. Tkinter possess three layout managers:

    pack
    grid
    place

The three layout managers pack, grid, and place should never be mixed in the same master window! Geometry managers serve various functions. They:

    arrange widgets on the screen
    register widgets with the underlying windowing system
    manage the display of widgets on the screen

Arranging widgets on the screen includes determining the size and position of components. Widgets can provide size and alignment information to geometry managers, but the geometry managers has always the final say on the positioning and sizing.

Pack
Pack is the easiest to use of the three geometry managers of Tk and Tkinter. Instead of having to declare precisely where a widget should appear on the display screen, we can declare the positions of widgets with the pack command relative to each other. The pack command takes care of the details. Though the pack command is easier to use, this layout managers is limited in its possibilities compared to the grid and place mangers. For simple applications it is definitely the manager of choice. For example simple applications like placing a number of widgets side by side, or on top of each other.

fill Option
In our example, we have packed three labels into the parent widget "root". We used pack() without any options. So pack had to decide which way to arrange the labels. As you can see, it has chosen to place the label widgets on top of each other and centre them. Furthermore, we can see that each label has been given the size of the text. If you want to make the widgets as wide as the parent widget, you have to use the fill=X option:

Padding
The pack() manager knows four padding options, i.e. internal and external padding and padding in x and y direction:

padx 	External padding, horizontally
pady 	External padding, vertically

ipadx 	Internal padding, horizontally.
ipady 	Internal padding, vertically

The default value in all cases is 0.

Example:
'''

from Tkinter import *

root = Tk()

# kp: with no fill option
Label(root, text="Red Sun", bg="red", fg="white").pack()
Label(root, text="Green Grass", bg="green", fg="black").pack()
Label(root, text="Blue Sky", bg="blue", fg="white").pack()

# kp: with fill=X
Label(root, text="=============", bg="white", fg="black").pack(fill=X)
Label(root, text=".pack(fill=X) used below", bg="white", fg="black").pack(fill=X)
Label(root, text="Red Sun", bg="red", fg="white").pack(fill=X)
Label(root, text="Green Grass", bg="green", fg="black").pack(fill=X)
Label(root, text="Blue Sky", bg="blue", fg="white").pack(fill=X)

#kp: External padding, horizontally
Label(root, text="=============", bg="white", fg="black").pack(fill=X)
Label(root, text="External horizontal padding: .pack(ipadx=10)", bg="white", fg="black").pack(fill=X)
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack(fill=X,padx=10)
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill=X,padx=10)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=X,padx=10)

#kp: External padding, vertically
#Label(root, text="=============", bg="white", fg="black").pack(fill=X)
Label(root, text="External vertical padding: .pack(ipady=10)", bg="white", fg="black").pack(fill=X)
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack(fill=X,pady=10)
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill=X,pady=10)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=X,pady=10)

#kp: Internal padding, horizontally
#Label(root, text="=============", bg="white", fg="black").pack(fill=X)
Label(root, text="Internal horizontal padding: .pack(ipadx=10)", bg="white", fg="black").pack(fill=X)
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack()
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(ipadx=10)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack()

#kp: Internal padding, vertically
#Label(root, text="=============", bg="white", fg="black").pack(fill=X)
Label(root, text="Internal vertical padding: .pack(ipady=10)", bg="white", fg="black").pack(fill=X)
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack()
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(ipady=10)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack()

#Placing widgets side by side
#We want to place the three label side by side now and shorten the text slightly:
Label(root, text="=============", bg="white", fg="black").pack(fill=X)
Label(root, text="Placing widgets side by side", bg="white", fg="black").pack(fill=X)
w = Label(root, text="red", bg="red", fg="white")
w.pack(padx=5, pady=10, side=LEFT)
w = Label(root, text="green", bg="green", fg="black")
w.pack(padx=5, pady=20, side=LEFT)
w = Label(root, text="blue", bg="blue", fg="white")
w.pack(padx=5, pady=20, side=LEFT)
#If we change LEFT to RIGHT in the previous example, we get the colours in reverse order:

mainloop()
