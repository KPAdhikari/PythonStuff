'''
The Canvas Image Item
The Canvas method create_image(x0,y0, options ...) is used to draw an image on a canvas. create_image doesn't accept an image directly. It uses an object which is created by the PhotoImage() method. The PhotoImage class can only read GIF and PGM/PPM images from files
'''

from tkinter import *

canvas_width = 300
canvas_height =300

master = Tk()

canvas = Canvas(master,
           width=canvas_width,
           height=canvas_height)
canvas.pack()

# kp: The following gif files are actually Animated gifs and if opened
#     with a browser, we'll see the animation (I think browsers have tools to play the animation)
#img = PhotoImage(file="rocks.ppm")
img = PhotoImage(file="AnimatedGIF_Art_mindWarping.gif")
img = PhotoImage(file="AnimatedGIF_Art_LookUniverse.gif")
canvas.create_image(20,20, anchor=NW, image=img)

mainloop()
