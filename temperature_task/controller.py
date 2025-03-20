class Controller:
    def __init__(self, model, view):
        self.__model = model
        self.__view = view

    def set_temperature_value(self):
        temperature_value = self.__view.prompt_for_temperature_value()

        try:
            self.__model.set_temperature_value(temperature_value)
        except ValueError:
            print("Переменная temperature_value не является числом")

    def set_to_scale(self):
        to_scale = self.__view.prompt_for_to_scale()

        try:
            str(self.__model.set_to_scale(to_scale))
        except TypeError:
            print("Переменная to_scale не является string")

    def set_from_scale(self):
        from_scale = self.__view.prompt_for_from_scale()

        try:
            str(self.__model.set_from_scale(from_scale))
        except TypeError:
            print("Переменная from_scale не является string")
