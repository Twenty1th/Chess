from typing import List

from coordinates import Coordinates
from .shape import Shape


class King(Shape):
    def move(self, coordinate):
        pass

    def get_available_moves(self) -> List[Coordinates]:
        pass