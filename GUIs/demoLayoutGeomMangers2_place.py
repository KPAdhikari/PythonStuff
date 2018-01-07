'''
https://www.python-course.eu/tkinter_layout_management.php
Place Geometry Manager
The Place geometry manager allows you explicitly set the position and size of a window, either in absolute terms, or relative to another window. The place manager can be accessed through the place method. It can be applied to all standard widgets.

We use the place geometry manager in the following example. We are playing around with colours in this example, i.e. we assign to every label a different colour, which we randomly create using the randrange method of the random module. We calculate the brightness (grey value) of each colour. If the brightness is less than 120, we set the foreground colour (fg) of the label to White otherwise to black, so that the text can be easier read.
'''

import Tkinter as tk
import random

root = tk.Tk()
# width x height + x_offset + y_offset:
root.geometry("170x200+30+30") #kp: it seems there cannot be any space around x & +
# kp: with the spaces, I got "_tkinter.TclError: bad geometry specifier "170 x 200 + 30 + 30""

languages = ['Python','Perl','C++','Java','Tcl/Tk']
labels = range(5) #kp: it's a list of 0, 1, 2, 3, 4

'''
List comprehensions: http://blog.teamtreehouse.com/python-single-line-loops
List comprehensions are lists that generate themselves with an internal for loop. They’re a very common feature in Python and they look something like:

[thing for thing in list_of_things]

see more below
'''

for i in range(5):
    #kp: Following line is a case of List Comprehension. Here, a list
    #    of 3 random integers between 0 and 255 (to represent color) is generated.
   ct = [random.randrange(256) for x in range(3)]
   brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
   ct_hex = "%02x%02x%02x" % tuple(ct)
   bg_colour = '#' + "".join(ct_hex)
   l = tk.Label(root,
                text=languages[i],
                fg='White' if brightness < 120 else 'Black',
                bg=bg_colour)
   l.place(x = 20, y = 30 + i*30, width=120, height=25)

root.mainloop()


'''
More on List comprehension:

List comprehensions save # of lines of code.

Let’s say I want to have a function that doubles the values all of the items in a list of numbers.

Equivalent code snippets

======== Code Snippet 1 ====
def list_doubler(lst):
    doubled = []
    for num in lst:
        doubled.append(num*2)
    return doubled

my_list = [21, 2, 93]
my_doubled_list = list_doubler(lst)

======== Code Snippet 2 ====
def list_doubler(lst):
    doubled = [num * 2 for num in lst]
    return doubled
my_list = [21, 2, 93]
my_doubled_list = list_doubler(lst)

======== Code Snippet 3 ====
my_list = [21, 2, 93]
my_doubled_list = [num * 2 for num in my_list]

'''
