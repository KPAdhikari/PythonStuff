'''
Drawing Polygons
If you want to draw a polygon, you have to provide at least three coordinate points:
create_polygon(x0,y0, x1,y1, x2,y2, ...)

In the following example we draw a triangle using this method:
'''

from tkinter import *

canvas_width = 200
canvas_height =200
python_green = "#476042"

master = Tk()

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

points = [0,0,canvas_width,canvas_height/2, 0, canvas_height]
w.create_polygon(points, outline=python_green,
            fill='yellow', width=3)

mainloop()
