from abc import abstractmethod, ABC
from typing import List

from coordinates import Coordinates
from enums import ShapeColors, ShapeUnicodes, HorizontalCoordinates, VerticalCoordinates


class Shape(ABC):

    _unicode_symbol: ShapeUnicodes
    _color: ShapeColors

    def __init__(self, *, coordinates: Coordinates, color: ShapeColors, unicode: ShapeUnicodes):
        self._color = color
        self._unicode_symbol = unicode
        self._coordinates = coordinates

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value: Coordinates):
        self._coordinates = value

    @property
    def color(self):
        return self._color

    @property
    def unicode(self):
        return self._unicode_symbol

    @abstractmethod
    def move(self, coordinate: Coordinates):
        ...

    @abstractmethod
    def get_available_moves(self) -> List[Coordinates]:
        ...

    def is_coordinate_available(self, new_coordinate: Coordinates) -> bool:
        if (new_coordinate.vertical > max(VerticalCoordinates) or
                new_coordinate.vertical < min(VerticalCoordinates) or
                new_coordinate.horizontal is None):
            return False
        return True

    def __repr__(self):
        return " " + (self._color + self._unicode_symbol) + " "
