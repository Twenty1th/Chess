from abc import abstractmethod, ABC
from typing import List, Tuple

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

    @property
    @abstractmethod
    def can_jump(self) -> bool:
        pass

    @abstractmethod
    def moves(self) -> List[Tuple[int, int]]:
        ...

    def get_available_moves(self) -> List[Coordinates]:
        k = {value.value: key for key, value in enumerate(HorizontalCoordinates)}
        coordinates = self.coordinates
        moves = []
        for horiz, vert in self.moves():
            new_horiz = k[coordinates.horizontal] + horiz
            if max(k.items(), key=lambda x: x[1])[1] < new_horiz or new_horiz < 0:
                continue
            new_vert = coordinates.vertical + vert
            new_coordinate = Coordinates(list(k.keys())[new_horiz], new_vert)
            if new_coordinate != coordinates:
                moves.append(new_coordinate)
        return list(filter(self.is_coordinate_available, moves))

    def is_coordinate_available(self, new_coordinate: Coordinates) -> bool:
        return not any(
            [(new_coordinate.vertical > max(VerticalCoordinates)),
             (new_coordinate.vertical < min(VerticalCoordinates)),
             (new_coordinate.horizontal is None)])

    def __repr__(self):
        return " " + (self._color + self._unicode_symbol) + " "
