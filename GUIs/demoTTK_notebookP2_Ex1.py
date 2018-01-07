# https://stackoverflow.com/questions/16514617/python-tkinter-notebook-widget
from Tkinter import *
from ttk import *

root = Tk()
scheduledimage=PhotoImage("AnimatedGIF_Art_mindWarping.gif")
note = Notebook(root)

tab1 = Frame(note)
tab2 = Frame(note)
tab3 = Frame(note)
Button(tab1, text='Exit', command=root.destroy).pack(padx=100, pady=100)

note.add(tab1, text = "Tab One",image=scheduledimage, compound=TOP)
note.add(tab2, text = "Tab Two")
note.add(tab3, text = "Tab Three")
note.pack()
root.mainloop()
exit()
