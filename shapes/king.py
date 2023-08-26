from typing import List

from coordinates import Coordinates
from .shape import Shape


class King(Shape):
    @property
    def can_jump(self) -> bool:
        return False

    def moves(self):
        pass
