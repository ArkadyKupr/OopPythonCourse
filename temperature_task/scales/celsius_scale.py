from temperature_task.scales.scale import Scale


class CelsiusScale(Scale):
    def get_temperature_abbreviation(self):
        return "C"

    def convert_to_celsius(self, temperature):
        return temperature

    def convert_from_celsius(self, temperature):
        return temperature

    def __repr__(self):
        return "C"
