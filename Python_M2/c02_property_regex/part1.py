# class Cube():
#     _unit = "inch"
#
#     def __init__(self, side):
#         self._side = side
#
#     def area(self):
#         return f"{self._side * self._side * 6} {self._unit}"
#
#     def substract_side(self, value):
#         if value >= self._side:
#             raise Exception
#         self._side -= value
#
#     def change_unit(self, unit):
#         if self._unit == "inch" and unit == "cm":  # this will scale !!!
#             self._unit = unit
#             self._side *= 2.54
#
#
# cube = Cube(10)
# print(cube.area())
# cube.change_unit('cm')
# cube.substract_side(11)
# print(cube.area())
#
# print(cube.area())


# class Cube():
#     _unit = "inch"
#     current_unit = "inch"
#     conversion = {'cm': 2.54, 'inch': 1}
#
#     def __init__(self, side):
#         self._side = side
#
#     def area(self):
#         return f"{self.side * self.side * 6} {self.current_unit}"
#
#     def substract_side(self, value):
#         if value >= self.side:
#             raise Exception
#         self.side -= value
#
#     def change_unit(self, unit):
#         self.current_unit = unit
#
#     def get_side(self):
#         return self.conversion[self.current_unit] * self._side
#
#     def set_side(self, value):
#         self._side = value / self.conversion[self.current_unit]
#
#     def del_side(self):
#         self._side = 0
#
#     side = property(get_side, set_side, del_side)
#
# cube = Cube(10)
# print(cube.side)
# cube.change_unit('cm')
# print(cube.side)
# cube.side = 10
# cube.substract_side(9)
#
# print(cube.area())


class Cube():
    _unit = "inch"
    current_unit = "inch"
    conversion = {'cm': 2.54, 'inch': 1}

    def __init__(self, side):
        self._side = side

    def area(self):
        return f"{self.side * self.side * 6} {self.current_unit}"

    def substract_side(self, value):
        if value >= self.side:
            raise Exception
        self.side -= value

    def change_unit(self, unit):
        self.current_unit = unit

    @property
    def side(self):
        return self.conversion[self.current_unit] * self._side

    @side.setter
    def side(self, value):
        self._side = value / self.conversion[self.current_unit]

    @side.deleter
    def side(self):
        self._side = 0


cube = Cube(10)
print(cube.side)
cube.change_unit('cm')
print(cube.side)
cube.side = 10
cube.substract_side(9)

print(cube.area())


class Temp():
    _unit = 'Kelvin'
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