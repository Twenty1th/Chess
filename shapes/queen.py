from typing import List

from coordinates import Coordinates
from .shape import Shape


class Queen(Shape):
    @property
    def can_jump(self) -> bool:
        return False

    def moves(self, coordinate):
        pass
