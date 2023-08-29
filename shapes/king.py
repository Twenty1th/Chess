from typing import List

from enums import MovesDirection
from .shape import Shape


class King(Shape):
    @property
    def direction_options(self) -> List[MovesDirection]:
        return []

    def moves(self):
        pass
