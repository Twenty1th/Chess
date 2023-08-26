from .shape import Shape


class Bishop(Shape):
    @property
    def can_jump(self) -> bool:
        return False

    def moves(self):
        return [(i, abs(i)) if j == 0 else (abs(i), i) for i in range(-7, 8) for j in range(0, 2)]
