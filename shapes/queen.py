from .shape import Shape


class Queen(Shape):
    @property
    def can_jump(self) -> bool:
        return False

    def moves(self):
        moves = []
        for i in range(-7, 8):
            moves.append([i, 0])
            moves.append([0, i])
            moves.append([i, i])
            moves.append([abs(i), i])
            moves.append([i, abs(i)])
        return moves
