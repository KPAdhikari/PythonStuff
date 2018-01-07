'''
Choosing a Colour
There are applications where the user should have the possibility to select a colour. Tkinter provides a pop-up menu to choose a colour. To this purpose we have to import the tkColorChooser module and have to use the method askColor:

result = tkColorChooser.askColor ( color, option=value, ...)

If the user clicks the OK button on the pop-up window, respectively, the return value of askColor() is a tuple with two elements, both a representation of the chosen colour, e.g. ((106, 150, 98), '#6a9662')
The first element return[0] is a tuple (R, G, B) with the RGB representation in decimal values (from 0 to 255). The second element return[1] is a hexadecimal representation of the chosen colour.
If the user clicks "Cancel" the method returns the tuple (None, None).

The optional keyword parameters are:
color 	The variable color is used to set the default colour to be displayed. If color is not set, the initial colour will be grey.
title 	The text assigned to the variable title will appear in the pop-up window's title area. The default title is "Color".
parent 	Make the pop-up window appear over window W. The default behaviour is that it appears over the root window.


Let's have a look at an example:
'''

from Tkinter import *
from tkColorChooser import askcolor

def callback():
    result = askcolor(color="#6A9662",
                      title = "Bernd's Colour Chooser")
    print result

root = Tk()
Button(root,
       text='Choose Color',
       fg="darkgreen",
       command=callback).pack(side=LEFT, padx=10)
Button(text='Quit',
       command=root.quit,
       fg="red").pack(side=LEFT, padx=10)
mainloop()

'''
The look and feel depends on the operating system (e.g. Linux or Windows) and the chosen GUI (GNOME, KDE and so on). The following windows appear, if you use Gnome:

Choosing a Colour Startmenu

Choosing a Colour with Tkinter and Python

Using the same script under Windows 7 gives us the following result:
Choosing a Colour the Windows 7 way
'''
