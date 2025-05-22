from abc import ABC, abstractmethod


class Scale(ABC):
    @abstractmethod
    def get_temperature_abbreviation(self):
        pass

    @abstractmethod
    def convert_from_celsius(self, temperature):
        pass

    @abstractmethod
    def convert_to_celsius(self, temperature):
        pass
