'''
https://www.python-course.eu/tkinter_canvas.php
Oval Objects
An oval (or an ovoid) is any curve resembling an egg (ovum means egg in Latin). It resembles an ellipse, but it is not an ellipse. The term "oval" is not well-defined. Many different curves are called ovals, but they all have in common:

    They are differentiable, simple (not self-intersecting), convex, closed, plane curves
    They are very similar in shape to ellipses
    There is at least one axis of symmetry

The word oval stems from Latin ovum meaning "egg" and that's what it is: A figure which resembles the form of an egg. An oval is constructed from two pairs of arcs, with two different radii A circle is a special case of an oval.

We can create an oval on a canvas c with the following method:

id = C.create_oval ( x0, y0, x1, y1, option, ... )

This method returns the object ID of the new oval object on the canvas C.

The following script draws a circle around the point (75,75) with the radius 25:
'''

from tkinter import *

canvas_width = 190
canvas_height =150

master = Tk()

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

w.create_oval(50,50,100,100)

mainloop()


'''
We can define a small function drawing circles by using the create_oval() method.

def circle(canvas,x,y, r):
   id = canvas.create_oval(x-r,y-r,x+r,y+r)
   return id
'''
