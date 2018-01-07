import tkinter as tk


class GuiOverlay:
    def __init__(self, parent):

        self.f1 = tk.Frame(parent, padx=2, pady=2, relief=tk.SUNKEN)
        self.f1.pack(side='left', fill='both', expand=True)

        self.f1_widgets = list()
        self.f1_numbuttons = 8
        self.f1_row = 1
        self.f1_col = 0

        self.f2 = tk.Frame(parent, padx=2, pady=2, relief=tk.SUNKEN)
        self.f2.pack(side='right', fill='both', expand=True)

        self.f2.widgets = list()

        self.build_f1()
        self.build_page1()
        self.build_page2()
        self.build_page3()
        self.show_page(self.page1)

    def add_sep(self, r, c, widg):
        tk.Label(widg).grid(row=r, column=c)

    def build_f1(self):
        self.lf1 = tk.Label(self.f1, text='PAGE SELECT')
        self.lf1.grid(row=0, column=0)
        b1 = tk.Button(self.f1, text="Page 1", command=lambda: self.show_page(self.page1), width=8, height=2)
        b1.grid(row=1, column=0)
        b2 = tk.Button(self.f1, text="Page 2", command=lambda: self.show_page(self.page2), width=8, height=2)
        b2.grid(row=2, column=0)
        b3 = tk.Button(self.f1, text="Edit", command=lambda: self.show_page(self.page3), width=8, height=2)
        b3.grid(row=3, column=0)
        b4 = tk.Button(self.f1, text="Reserved", command=self.pass_function, width=8, height=2)
        b4.grid(row=4, column=0)
        b5 = tk.Button(self.f1, text="Reserved", command=self.pass_function, width=8, height=2)
        b5.grid(row=5, column=0)
        b6 = tk.Button(self.f1, text="Reserved", command=self.pass_function, width=8, height=2)
        b6.grid(row=6, column=0)
        b7 = tk.Button(self.f1, text="Reserved", command=self.pass_function, width=8, height=2)
        b7.grid(row=7, column=0)
        b8 = tk.Button(self.f1, text="Reserved", command=self.pass_function, width=8, height=2)
        b8.grid(row=8, column=0)

    def build_page1(self):
        self.page1 = tk.Frame(self.f2, padx=2, pady=2, relief=tk.SUNKEN)
        self.page1.grid(row=0, column=0, sticky='nsew')

        p1l1 = tk.Label(self.page1, text='This is page1')
        p1l1.grid(row=0, column=0)

        self.page1.lower()

    def build_page2(self):
        self.page2 = tk.Frame(self.f2, padx=2, pady=2, relief=tk.SUNKEN)
        self.page2.grid(row=0, column=0, sticky='nsew')

        p2l1 = tk.Label(self.page2, text='This is page2')
        p2l1.grid(row=0, column=0)

        up_button = tk.Button(self.page2, text="up")
        up_button.grid(row=1, column=0)

        temp_setpoint_label = tk.Label(self.page2, text="75")
        temp_setpoint_label.grid(row=1, column=1)

        down_button = tk.Button(self.page2, text="dn")
        down_button.grid(row=1, column=2)

        self.page2.lower()

    def build_page3(self):
        self.page3 = tk.Frame(self.f2, padx=2, pady=2, relief=tk.SUNKEN)
        self.page3.grid(row=0, column=0, sticky='nsew')

        p3l1 = tk.Label(self.page3, text='Most Excellent Edit Page')
        p3l1.grid(row=0, column=0)

        p3tx = tk.Text(self.page3)
        p3tx.grid(row=1, column=0, sticky='nsew')

        self.page2.lower()

    def show_page(self, pageno):
        pageno.lift()

    def pass_function(self):
        pass


def main():
    root = tk.Tk()
    # root.geometry("800x400")
    root.title('Try GUI overlay')
    GuiOverlay(root)
    root.mainloop()


if __name__ == '__main__':
    main()
