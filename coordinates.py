from collections import namedtuple


class Coordinates(namedtuple('Coordinates', 'horizontal vertical')):
    def __new__(cls, horizontal: str, vertical: int):
        return super(Coordinates, cls).__new__(cls, horizontal, vertical)
