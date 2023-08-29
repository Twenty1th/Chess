from typing import List

from shapes.moves_filter import MovesFilter
from shapes.shape import Shape
from shapes.shape_factory import ShapeFactory
from square import Square
from coordinate import Coordinate
from enums import HorizontalCoordinates, VerticalCoordinates

board = List[List[Square]]


class Board(board):

    def __init__(self):
        super().__init__()
        rows = [[Square(coordinates=Coordinate(horizontal, vertical),
                        shape=ShapeFactory.get_shape_by_coordinates(coordinates=Coordinate(horizontal, vertical)))
                 for horizontal in HorizontalCoordinates]
                for vertical in VerticalCoordinates]
        self.extend(rows)

    def __getitem__(self, item: int | slice | Coordinate):
        if isinstance(item, int):
            adjusted_index = item - 1
            if 0 <= adjusted_index < len(self):
                return super().__getitem__(adjusted_index)
            else:
                raise IndexError("Index out of range")
        elif isinstance(item, Coordinate):
            row = self[item.vertical]
            return row[HorizontalCoordinates.get_index(item.horizontal)]

        return super().__getitem__(item)

    def is_have_shape_by_coordinate(self, coordinate: Coordinate) -> bool:
        return self[coordinate].shape is not None

    def get_shape_by_coordinate(self, coordinate: Coordinate) -> Shape:
        return self[coordinate].shape

    def change_square_shape(self, coordinate: Coordinate, new_shape: Shape):
        new_shape.coordinate = coordinate
        self[coordinate].shape = new_shape

    def rm_shape_from_square(self, shape: Shape):
        self[Coordinate(shape.coordinate.horizontal, shape.coordinate.vertical)].rm_shape()

    def get_shape_moves(self, shape: Shape) -> List[Coordinate]:  # noqa
        return MovesFilter.filter(self, shape)

    def coordinate_is_available(self, coordinate: Coordinate):
        return self[coordinate].shape is None

    def move(self, shape: Shape, to: Coordinate):
        self.rm_shape_from_square(shape)
        self.change_square_shape(to, shape)

    def __repr__(self):
        output = ""

        for num, row in zip(list(VerticalCoordinates)[::-1], self[::-1]):
            output += f"{num}  " + "".join([f"{square}" for square in row])
            output += "\n"
        output += "    " + "  ".join(HorizontalCoordinates)

        return output
