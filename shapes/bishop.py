from typing import List

from enums import MovesDirection
from .shape import Shape


class Bishop(Shape):
    @property
    def direction_options(self) -> List[MovesDirection]:
        return [MovesDirection.TOP_LEFT, MovesDirection.DOWN_LEFT,
                MovesDirection.TOP_RIGHT, MovesDirection.DOWN_RIGHT]

    def moves(self):
        moves = []
        for i in range(-7, 8):
            moves.append((i, abs(i)))
            moves.append((abs(i), i))
            moves.append((i, i))
        return moves
