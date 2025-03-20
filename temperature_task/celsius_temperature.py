from temperature_task.temperature import Temperature
from tkinter.messagebox import showerror


class CelsiusTemperature(Temperature):
    def __init__(self, temperature):
        self.__temperature = temperature

    @property
    def temperature_scale(self):
        return "C"

    def convert_temperature_to_celsius_scale(self):
        try:
            float(self.__temperature)
        except ValueError:
            showerror("Error", "The value entered is not a number")

        return float(self.__temperature)

    def convert_temperature_from_celsius_scale(self):
        try:
            float(self.__temperature)
        except ValueError:
            showerror("Error", "The value entered is not a number")

        return float(self.__temperature)
