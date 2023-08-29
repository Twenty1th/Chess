from typing import Optional, List, Callable

from board import Board
from coordinate import Coordinate
from shapes.shape import Shape


class Game:

    def __init__(self):
        self.board = Board()

    def start(self):
        while True:
            print("CTRL + C to exit from a game")
            print(self.board)
            move: str = input("Input coordinate(ex A1, C2): ")
            if (coordinate := self.unparse_input_to_coordinate(move)) is None:
                continue
            if (shape := self.board.get_shape_by_coordinate(coordinate)) is None:
                print("Coordinate has not shape")
                continue
            moves = self.board.get_shape_moves(shape)
            if not moves:
                print("Shape has not moves")
                continue

            shape_move = input(f"Input next move from available ({moves}): ")

            if (shape_move_coordinate := self.unparse_input_to_coordinate(shape_move)) is None:
                continue
            if shape_move_coordinate not in moves:
                print("Not available coordinate")

            self.board.move(shape, shape_move_coordinate)

    @staticmethod
    def unparse_input_to_coordinate(move: str) -> Optional[Coordinate]:
        try:
            coordinate = Coordinate(move[0], int(move[1]))
            return coordinate
        except Exception:
            print("Unrecognized coordinate")
            return None
