from .shape import Shape


class King(Shape):
    @property
    def can_jump(self) -> bool:
        return False

    def moves(self):
        pass
