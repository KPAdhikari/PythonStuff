#https://stackoverflow.com/questions/7299955/tkinter-binding-a-function-with-arguments-to-a-widget
from Tkinter import *

def rand_func(eff=None,a=1,b=2,c=3):
    print (a+b+c)

root=Tk()
root.bind("<Return>",lambda eff:rand_func(eff,a=10,b=20,c=30))

frame=Frame(root)
frame.pack()

button1=Button(frame, text="click me 1", command=lambda:rand_func(None,1,2,3))
button1.pack()
button2=Button(frame, text="click me 2", command=lambda:rand_func(None,7,8,9))
button2.pack()

root.mainloop()
