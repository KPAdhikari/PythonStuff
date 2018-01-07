#https://stackoverflow.com/questions/42934717/issue-in-applying-geometry-grid-to-widgets-in-tkinter-notebook-pages
import Tkinter
from Tkinter import *
import ttk
from ttk import *

app = Tk()
app.configure(background='DimGray')
app.geometry('600x600')
app.resizable(width=False, height=False)

note = Notebook(app)

tab1 = Frame(note)
tab2 = Frame(note)
tab3 = Frame(note)

note.add(tab1, text = "Tracing", compound=TOP)
note.add(tab2, text = "Network Details")
note.add(tab3, text = "Tab Three")
note.pack(fill=BOTH, expand=True)

lb1 = Label(tab1,  text="Trace Object")
lb1.grid(row=1, column=1, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
lb1.pack()

variable = StringVar(app)
variable.set("Select From List")

cm = ttk.Combobox(tab1, textvariable=variable)
cm.config(values =('Select From Phase A', 'Select From Phase B'))
cm.grid(row=1, column=2, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
cm.pack()

app.mainloop()
