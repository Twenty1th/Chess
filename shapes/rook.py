from .shape import Shape


class Rook(Shape):
    @property
    def can_jump(self):
        return False

    def moves(self):
        return [(0, i) if j == 0 else (i, 0) for i in range(-7, 8) for j in range(0, 2)]
