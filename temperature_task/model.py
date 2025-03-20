class Model:
    def __init__(self):
        self.__temperature_value = 0
        self.__to_scale = None
        self.__from_scale = None

    def set_temperature_value(self, temperature_value):
        self.__temperature_value = temperature_value

    def get_temperature_value(self):
        return self.__temperature_value

    def set_to_scale(self, to_scale):
        self.__to_scale = to_scale

    def get_to_scale(self):
        return self.__to_scale

    def set_from_scale(self, from_scale):
        self.__from_scale = from_scale

    def get_from_scale(self):
        return self.__from_scale
