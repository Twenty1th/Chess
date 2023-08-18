from typing import List

from coordinates import Coordinates
from enums import HorizontalCoordinates
from .shape import Shape


class Knight(Shape):
    def move(self, coordinate):
        pass

    def get_available_moves(self) -> List[Coordinates]:
        k = {value.value: key for key, value in enumerate(HorizontalCoordinates)}
        coordinates = self.coordinates
        moves = []
        for horiz, vert in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-1, 2), (-2, 1)]:
            new_horiz = k[coordinates.horizontal] + horiz
            if max(k.items(), key=lambda x: x[1])[1] < new_horiz or new_horiz < 0:
                continue
            new_vert = coordinates.vertical + vert
            new_coordinate = Coordinates(list(k.keys())[new_horiz], new_vert)
            moves.append(new_coordinate)
        return list(filter(self.is_coordinate_available, moves))
