#!/usr/bin/python3

from tkinter import *
fields = 'Last Name', 'First Name', 'Job', 'Country'

def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text))

def makeform(root, fields):
   entries = []
   for field in fields:
      #kp: http://effbot.org/tkinterbook/frame.htm
      row = Frame(root)

      #kp: https://www.tutorialspoint.com/python/tk_anchors.htm
      #kp: Anchors are used to define where text is positioned relative to a reference point.
      #kp: s, e, w, N, NE etc mean South, East, West, North, North-East etc
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)

      #kp: http://effbot.org/tkinterbook/pack.htm
      #kp: You can use the fill=X option to make all widgets as wide as the parent widget:
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)

   # Lambda Functions: http://www.secnetix.de/olli/Python/lambda_functions.hawk
   # Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, using a construct called "lambda". This is not exactly the same as lambda in functional programming languages, but it is a very powerful concept that's well integrated into Python and is often used in conjunction with typical functional concepts like filter(), map() and reduce().

      '''
   # Events and Bindings: http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
   As was mentioned earlier, a Tkinter application spends most of its time inside an event loop (entered via the mainloop method). Events can come from various sources, including key presses and mouse operations by the user, and redraw events from the window manager (indirectly caused by the user, in many cases).

Tkinter provides a powerful mechanism to let you deal with events yourself. For each widget, you can bind Python functions and methods to events.

widget.bind(event, handler)

If an event matching the event description occurs in the widget, the given handler is called with an object describing the event.
   '''
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))
   b1 = Button(root, text='Show',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
