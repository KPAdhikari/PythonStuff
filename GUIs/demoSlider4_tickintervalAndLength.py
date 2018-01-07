'''
tickinterval and length
If the option tickinterval is set to a number, the ticks of the scale will be displayed as multiples of that value. We add a tickinterval to our previous example.
'''

#from Tkinter import *
from tkinter import *

def show_values():
    print (w1.get(), w2.get())

master = Tk()
w1 = Scale(master, from_=0, to=42, tickinterval=8)
w1.set(19)
w1.pack()

# To be able to see the numbers on the horizontal slider, use the second line (with length) below
#w2 = Scale(master, from_=0, to=200,tickinterval=10, orient=HORIZONTAL)
w2 = Scale(master, from_=0, to=200, length=600,tickinterval=10, orient=HORIZONTAL)
w2.set(23)
w2.pack()
Button(master, text='Show', command=show_values).pack()

mainloop()

'''
If we start this program, we recognize that the vertical slider has the values 0, 8, 16, 24, 32, 40 added to its left side. The horizontal slider has also the numbers 0,10,20, 30, ..., but we can't see them, because the get smeared on top of each other, because the slider is not long enough:

To solve this problem we have to increase the length of our horizontal slider. We set the option length. length defines the x dimension, if the scale is horizontal and the y dimension, if the scale is vertical. So we change the definition of w2 in the following way:
w2 = Scale(master, from_=0, to=200, length=600,tickinterval=10, orient=HORIZONTAL)

'''
