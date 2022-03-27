class Temp:
    current_unit = 'Kelvin'
    conversion = {'Celsius': 273.15, 'Kelvin': 0}

    def __init__(self, t):
        self._t = t

    def substract_temp(self, value):
        if value >= self._t:
            raise Exception
        self._t -= value

    def change_unit(self, unit):
        self.current_unit = unit

    @property
    def temperature(self):
        return self._t - self.conversion[self.current_unit]

    @temperature.setter
    def temperature(self, value):
        self._t = value + self.conversion[self.current_unit]

    @temperature.deleter
    def temperature(self):
        self._t = 0


temp = Temp(10)
print(temp.temperature)
temp.change_unit('Celsius')
print(temp.temperature)
temp.substract_temp(1)
print(temp.temperature)
