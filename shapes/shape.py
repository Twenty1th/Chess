from abc import abstractmethod, ABC
from typing import List, Tuple

from coordinate import Coordinate
from enums import ShapeColors, ShapeUnicodes, HorizontalCoordinates, VerticalCoordinates, MovesDirection


class Shape(ABC):

    _unicode_symbol: ShapeUnicodes
    _color: ShapeColors

    def __init__(self, *, coordinates: Coordinate, color: ShapeColors, unicode: ShapeUnicodes):
        self._color = color
        self._unicode_symbol = unicode
        self._coordinate = coordinates

    @property
    def coordinate(self):
        return self._coordinate

    @coordinate.setter
    def coordinate(self, value: Coordinate):
        self._coordinate = value

    @property
    def color(self):
        return self._color

    @property
    def unicode(self):
        return self._unicode_symbol

    @property
    @abstractmethod
    def direction_options(self) -> List[MovesDirection]:
        pass

    @abstractmethod
    def moves(self) -> List[Tuple[int, int]]:
        ...

    def get_available_coordinates_to_move(self) -> List[Coordinate]:
        coordinate = self.coordinate
        moves = []
        for horiz, vert in self.moves():
            new_horiz = HorizontalCoordinates.get_index(coordinate.horizontal) + horiz
            if HorizontalCoordinates.get_index(HorizontalCoordinates.H) < new_horiz or new_horiz < 0:
                continue
            new_vert = coordinate.vertical + vert
            new_coordinate = Coordinate(HorizontalCoordinates.get_value_by_index(new_horiz), new_vert)
            if new_coordinate != coordinate and new_coordinate not in moves:
                moves.append(new_coordinate)
        return list(filter(self.is_coordinate_available, moves))

    def is_coordinate_available(self, new_coordinate: Coordinate) -> bool: # noqa
        return all(
            [(min(VerticalCoordinates) <= new_coordinate.vertical <= max(VerticalCoordinates)),
             (new_coordinate.horizontal is not None)]
        )

    def __repr__(self):
        return " " + (self._color + self._unicode_symbol) + " "
