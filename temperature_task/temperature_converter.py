import tkinter.ttk
from temperature_task.controller import Controller
from temperature_task.model import Model
from temperature_task.view import View


class TemperatureConverter(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title("Temperature conversion")
        self.resizable(False, False)

        # create a model
        temperature_scales = ("C", "K", "F")
        model = Model()

        # create a view and place it on the root window
        view = View(temperature_scales)

        view.pack()

        # create a controller
        controller = Controller(model, view)
        controller.set_to_scale()
        controller.set_from_scale()
        controller.set_temperature_value()

        # set the controller to view
        view.set_controller(controller)
