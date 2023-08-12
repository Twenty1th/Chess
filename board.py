from typing import List

from square import Square
from shape import Shape
from coordinates import Coordinates
from enums import HorizontalCoordinates, VerticalCoordinates


class Board:

    def __init__(self):
        self.board: List[List[Square]] = []
        for horizontal in HorizontalCoordinates:
            row = [Square(coordinates=Coordinates(horizontal, vertical), shape=Shape())
                   for vertical in VerticalCoordinates]
            self.board.append(row)

    def __repr__(self):
        output = ""

        for row in self.board[::-1]:
            output += "".join([str(square) for square in row])
            output += "\n"

        return output

