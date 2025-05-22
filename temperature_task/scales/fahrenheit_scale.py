from temperature_task.scales.scale import Scale


class FahrenheitScale(Scale):
    def get_temperature_abbreviation(self):
        return "F"

    def convert_to_celsius(self, temperature):
        return round(((float(temperature) - 32) * 5 / 9), 2)

    def convert_from_celsius(self, temperature):
        return round((float(temperature) * 9 / 5 + 32), 2)

    def __repr__(self):
        return "F"
