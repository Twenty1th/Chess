from .shape import Shape


class Knight(Shape):
    @property
    def can_jump(self) -> bool:
        return True

    def moves(self):
        return [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-1, 2), (-2, 1)]
