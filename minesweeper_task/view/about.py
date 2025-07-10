import tkinter
from tkinter import ttk


class About(tkinter.ttk.Frame):
    def __init__(self, master=None, parent=None):
        super().__init__(master)
        frame = tkinter.ttk.Frame(self)
        frame.pack()

        self.parent = parent
        self.label = ttk.Label(frame, justify=tkinter.CENTER, relief=tkinter.FLAT, borderwidth=10, font=("Arial", 10),
                               text="This game \"Minesweeper\" was created as part of \n the \"OOP Python\" course")
        self.label.pack()

        self.master.title("About")
        self.master.resizable(True, True)
        self.master.minsize(300, 40)
        self.master.maxsize(400, 40)
        self.pack()

        self.focus_set()
