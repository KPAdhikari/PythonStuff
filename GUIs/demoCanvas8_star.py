'''
As we have mentioned, this approach is very unskilful. What if we have to change the size or the thickness of the star? We have to change all the points manually, which is of course an error-prone and tedious task to do. So, we present a new version of the previous script which involves more "programming" and programming skills. First, we put the creation of the star in a function, and we use an origin point and two lengths p and t to create the star:
Our new improved program looks like this now:
'''

from tkinter import *

canvas_width = 400
canvas_height =400
python_green = "#476042"

def polygon_star(canvas, x,y,p,t, outline=python_green, fill='yellow', width = 1):
   points = []
   for i in (1,-1):
      points.extend((x,	      y + i*p))
      points.extend((x + i*t, y + i*t))
      points.extend((x + i*p, y))
      points.extend((x + i*t, y - i * t))

   print(points)

   canvas.create_polygon(points, outline=outline,
                         fill=fill, width=width)

master = Tk()

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

p = 50
t = 15

nsteps = 10
step_x = int(canvas_width / nsteps)
step_y = int(canvas_height / nsteps)

for i in range(1, nsteps):
   polygon_star(w,i*step_x,i*step_y,p,t,outline='red',fill='gold', width=3)
   polygon_star(w,i*step_x,canvas_height - i*step_y,p,t,outline='red',fill='gold', width=3)

mainloop()

'''
The result looks even more like Xmas and we are sure that nobody doubts that it would be hell to define the polygon points directly, as we did in our first star example:
'''
