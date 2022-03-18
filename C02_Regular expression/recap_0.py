from typing import Union
# Versiunea extinsa
#
#
# class Length:
#     def __init__(self, length: Union[int, float]):
#         self._length = length
#
#     def get_length(self):
#         return self._length
#
#     def set_length(self, length: Union[int, float]):
#         self._length = length
#
#     def del_length(self):
#         del self._length
#
#     length = property(get_length, set_length, del_length)
#
#
# lungime = Length(100)
# print(lungime.length)
# lungime.length = 50
# print(lungime.length)
# # del lungime.length
# # print(lungime.length)


# Versiunea compacta
class Length:
    def __init__(self, length: Union[int, float]):
        self.__length = length

    @property
    def length(self):
        """ Returns the private/protected atribute of something."""
        return self.__length

    @length.setter
    def length(self, length: Union[int, float]):
        """ Sets the private/protected atribute of something."""
        self.__length = length

    @length.deleter
    def length(self):
        """ Deletes the private/protected atribute of something."""
        del self.__length


lungime = Length(100)
print(lungime.length)
lungime.length = 50
print(lungime.length)
# del lungime.length
# print(lungime.length)
