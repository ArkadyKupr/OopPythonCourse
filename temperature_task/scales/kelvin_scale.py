from temperature_task.scales.scale import Scale


class KelvinScale(Scale):
    def get_temperature_abbreviation(self):
        return "K"

    def convert_to_celsius(self, temperature):
        return round((float(temperature) - 273.15), 2)

    def convert_from_celsius(self, temperature):
        return round((float(temperature) + 273.15), 2)

    def __repr__(self):
        return "K"
