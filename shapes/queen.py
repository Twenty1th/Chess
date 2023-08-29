from typing import List

from enums import MovesDirection
from .shape import Shape
from itertools import combinations


class Queen(Shape):
    @property
    def direction_options(self) -> List[str]:
        return [MovesDirection.TOP, MovesDirection.DOWN,
                MovesDirection.DOWN_RIGHT, MovesDirection.DOWN_LEFT,
                MovesDirection.TOP_RIGHT, MovesDirection.TOP_LEFT,
                MovesDirection.LEFT, MovesDirection.RIGHT]

    def moves(self):
        top_moves = [(0, i) for i in range(1, 8)]
        down_moves = [(0, i) for i in range(-7, 0)]
        down_left_moves = [(i, i) for i in range(-7, 0)]
        down_right_moves = [(abs(i), i) for i in range(-7, 0)]
        top_right_moves = [(i, i) for i in range(1, 8)]
        top_left_moves = [(i, abs(i)) for i in range(-7, 0)]
        left_moves = [(i, 0) for i in range(-7, 0)]
        right_moves = [(i, 0) for i in range(1, 8)]
        return top_left_moves + top_moves + top_right_moves + down_right_moves + down_left_moves + down_moves + left_moves + right_moves
