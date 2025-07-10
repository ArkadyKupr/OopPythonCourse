import tkinter
from tkinter import ttk


class Records(tkinter.ttk.Frame):
    def __init__(self, master=None, parent=None):
        super().__init__(master)

        frame_1 = tkinter.ttk.Frame(self)
        self.frame_2 = tkinter.ttk.Frame(self)

        frame_1.pack()
        self.frame_2.pack()

        self.parent = parent

        self.show_record_table()

        self.master.title("Records")
        self.master.resizable(False, False)
        self.pack()

        self.focus_set()

    def show_record_table(self):
        with open("output.txt", "r", encoding="utf-8") as file:
            lines = [line.rstrip() for line in file]

        k = 0

        for i in range(1):
            for j in range(10):
                if k < len(lines):
                    self.name_and_time_record_button = ttk.Button(self.frame_2, text=f"{k + 1}. {lines[k]}", width=30)
                    self.name_and_time_record_button.grid(row=j, column=i)

                    k += 1
                else:
                    self.name_and_time_record_button = ttk.Button(self.frame_2, text=f" ", width=30)
                    self.name_and_time_record_button.grid(row=j, column=i)
