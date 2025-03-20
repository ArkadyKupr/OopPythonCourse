from abc import ABC, abstractmethod


class Temperature(ABC):
    @abstractmethod
    def convert_temperature_from_celsius_scale(self):
        pass

    @abstractmethod
    def convert_temperature_to_celsius_scale(self):
        pass
