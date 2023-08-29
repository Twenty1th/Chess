from typing import List

from enums import MovesDirection
from .shape import Shape


class Rook(Shape):

    @property
    def direction_options(self) -> List[MovesDirection]:
        return [MovesDirection.TOP, MovesDirection.DOWN,
                MovesDirection.LEFT, MovesDirection.RIGHT]

    def moves(self):
        return [(0, i) if j == 0 else (i, 0) for i in range(-7, 8) for j in range(0, 2)]
