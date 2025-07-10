import tkinter
from tkinter import ttk
from model.model import Model
from view.view import View
from controller.controller import Controller


class Minesweeper(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title("Minesweper")
        self.geometry("800x600")
        self.resizable(True, True)
        self.minsize(300, 200)
        self.maxsize(1200, 800)

        # создание model
        model = Model()

        # создание view_and_controller
        view = View()
        view.pack()

        # создание контроллера
        controller = Controller(model, view)
        controller.set_field_size()
        controller.set_mines_count()
        view.set_controller(controller)
