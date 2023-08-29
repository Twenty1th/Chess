from typing import List

from enums import MovesDirection
from .shape import Shape


class Knight(Shape):
    @property
    def direction_options(self) -> List[MovesDirection]:
        return [MovesDirection.JUMP]

    def moves(self):
        return [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-1, 2), (-2, 1)]
