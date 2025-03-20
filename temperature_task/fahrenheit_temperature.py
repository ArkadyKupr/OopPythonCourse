from temperature_task.temperature import Temperature
from tkinter.messagebox import showerror


class FahrenheitTemperature(Temperature):
    def __init__(self, temperature):
        self.__temperature = temperature

    @property
    def temperature_scale(self):
        return "F"

    def convert_temperature_to_celsius_scale(self):
        try:
            float(self.__temperature)
        except ValueError:
            showerror("Error", "The value entered is not a number")

        return round(((float(self.__temperature) - 32) * 5 / 9), 2)

    def convert_temperature_from_celsius_scale(self):
        try:
            float(self.__temperature)
        except ValueError:
            showerror("Error", "The value entered is not a number")

        return round((float(self.__temperature) * 9 / 5 + 32), 2)
