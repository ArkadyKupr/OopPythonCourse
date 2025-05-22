from temperature_task.scales.celsius_scale import CelsiusScale
from temperature_task.scales.fahrenheit_scale import FahrenheitScale
from temperature_task.scales.kelvin_scale import KelvinScale


class Model:
    def __init__(self):
        self.__temperatures = [CelsiusScale(), KelvinScale(), FahrenheitScale()]

    def get_temperatures(self):
        return self.__temperatures

    def set_from_scale(self, temperatures):
        self.__temperatures = temperatures
