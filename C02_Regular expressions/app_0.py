class Cube():
    _unit = "inch"
    current_unit = "inch"
    conversion = {'cm': 2.54, 'inch': 1}

    def __init__(self, side):
        self._side = side

    def area(self):
        return f"{self._side * self._side * 6} {self._unit}"
    def substract_side(self, value):
        if value >= self._side:
            raise Exception
        self._side -= value

    def change_unit(self, unit):
        self.current_unit = unit

    def get_side(self):
        return self.conversion[self.current_unit] * self._side

    def set_side(self, value):
        self._side = value / self.conversion[self.current_unit]

    def del_side(self):
        self._side = 0
    side = property(get_side, set_side, del_side)

cube = Cube(10)
print(cube.side)
cube.change_unit('cm')
print(cube.side)
cube.side = 20
print(cube.area())