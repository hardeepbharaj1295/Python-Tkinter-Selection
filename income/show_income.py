from tkinter import *
from tkinter.ttk import Treeview
import db.db


class ShowIncome:

    def __init__(self):
        self.win = Tk()
        canvas = Canvas(self.win, width=800, height=400, bg='white')
        canvas.pack(expand=YES, fill=BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()

        x = int(width / 2 - 800 / 2)
        y = int(height / 2 - 400 / 2)

        str1 = "800x400+" + str(x) + "+" + str(y)
        self.win.geometry(str1)
        self.win.resizable(width=False, height=False)
        self.win.title("Show Income | Administrator")

    def add_frame(self):

        self.frame = Frame(self.win, width=600, height=350)
        self.frame.place(x=80, y=20)

        x, y = 70, 20

        # use treeview to show the data in forms of table
        #mention the number of columns
        self.tr = Treeview(self.frame, columns=('A','B','C','D'), selectmode="extended")
        # heading key + text
        self.tr.heading('#0', text='Sr No')
        self.tr.column('#0', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#1', text='Source')
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#2', text='Description')
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#3', text='Update')
        self.tr.column('#3', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#4', text='Delete')
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)

        j = 0
        for i in db.db.show_income():
            self.tr.insert('',index=j, text=i[0], values=(i[1], i[2], 'Update', 'Delete'))
            j+=1

        self.tr.place(x=50, y = y + 50)

        self.win.mainloop()