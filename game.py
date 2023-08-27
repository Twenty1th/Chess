from typing import Optional, List

from board import Board
from coordinates import Coordinates
from shapes.shape import Shape


class Game:

    def __init__(self):
        self.board = Board()

    def start(self):
        while True:
            print(self.board)

            coordinate = self.get_input_coordinate()
            if not isinstance(coordinate, Coordinates):
                continue

            shape = self.get_shape_by_coordinates(coordinate)
            if shape is None:
                continue

            self.move_shape(shape)

    @staticmethod
    def get_input_coordinate() -> Coordinates | str | None:
        move = input("Input coordinate(ex A1, C2): ")
        if move == 'Back':
            return "Back"
        try:
            coordinate = Coordinates(move[0], int(move[1]))
            return coordinate
        except Exception:
            print("Unrecognized coordinate")
            return None

    def get_shape_by_coordinates(self, coordinates: Coordinates) -> Optional[Shape]:
        if (shape := self.board.get_shape_by_coordinate(coordinates)) is None:
            print("Coordinate has not shape")
        return shape

    def get_shape_moves(self, shape: Shape):
        return self.board.get_shape_moves(shape)

    def move_shape(self, shape: Shape):
        coordinates: List[Coordinates] = self.get_shape_moves(shape)
        while True:
            print(self.board)

            print("If you want change shape write command 'Back'")
            print(f"Input next move from available ({coordinates}): ")

            coordinate = self.get_input_coordinate()

            if not coordinate:
                break

            if coordinate not in coordinates:
                print("Not available coordinate")
                break

            self.board.move(shape, coordinate)
            break
