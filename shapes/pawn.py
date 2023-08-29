from typing import List

from enums import ShapeColors, MovesDirection
from .shape import Shape


class Pawn(Shape):
    @property
    def direction_options(self) -> List[MovesDirection]:
        return [MovesDirection.TOP]

    def moves(self):
        return [(0, 1), (0, 2) if self.color == ShapeColors.WHITE else (0, -1), (0, -2)]
