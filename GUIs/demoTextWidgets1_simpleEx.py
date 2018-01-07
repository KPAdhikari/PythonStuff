'''
https://www.python-course.eu/tkinter_text_widget.php
A text widget is used for multi-line text area. The Tkinter text widget is very powerful and flexible and can be used for a wide range of tasks. Though one of the main purposes is to provide simple multi-line areas, as they are often used in forms, text widgets can also be used as simple text editors or even web browsers.

Furthermore, text widgets can be used to display links, images, and HTML, even using CSS styles.

In most other tutorials and text books, it's hard to find a very simple and basic example of a text widget. That's why we want to start our chapter with a such an example:

We create a text widget by using the Text() method. We set the height to 2, i.e. two lines and the width to 30, i.e. 30 characters. We can apply the method insert() on the object T, which the Text() method had returned, to include text. We add two lines of text.
'''

#from Tkinter import *
from tkinter import *

root = Tk()
T = Text(root, height=2, width=30)
T.pack()
#T.insert(END, "Just a text Widget\nin two lines\n")

#Let's change our little example a tiny little bit. We add another text, the beginning of the famous monologue from Hamlet:
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
T.insert(END, quote)

mainloop()

'''
f we start our little script, we get a very unsatisfying result. We can see in the window only the first line of the monologue and this line is even broken into two lines. We can see only two lines in our window, because we set the height to the value 2. Furthermpre, the width is set to 30, so Tkinter has to break the first line of the monologue after 30 characters.

One solution to our problem consists in setting the height to the number of lines of our monologue and set width wide enough to display the widest line completely.

But there is a better technique, which you are well acquainted with from your browser and other applications: scrolling
'''
