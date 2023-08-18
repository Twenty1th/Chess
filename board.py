from typing import List

from shapes.shape import Shape
from shapes.shape_factory import ShapeFactory
from square import Square
from coordinates import Coordinates
from enums import HorizontalCoordinates, VerticalCoordinates, ShapeColors


board = List[List[Square]]


class Board(board):

    def __init__(self):
        super().__init__()
        for vertical in VerticalCoordinates:
            row = [Square(coordinates=Coordinates(horizontal, vertical),
                          shape=ShapeFactory.get_shape_by_coordinates(coordinates=Coordinates(horizontal, vertical)))
                   for horizontal in HorizontalCoordinates]
            self.append(row)

    def __getitem__(self, item):
        if isinstance(item, int):
            return super().__getitem__(item - 1)
        return super().__getitem__(item)

    def is_have_shape_by_coordinate(self, coordinate: Coordinates) -> bool:
        k = {value: key for key, value in enumerate(HorizontalCoordinates)}
        return self[coordinate.vertical][k[coordinate.horizontal]].shape is not None

    def is_have_coordinate_enemy_shape(self, coordinate: Coordinates, selected_shape_color: ShapeColors) -> bool:
        k = {value: key for key, value in enumerate(HorizontalCoordinates)}
        return self[coordinate.vertical][k[coordinate.horizontal]].shape.color == selected_shape_color

    def get_shape_by_coordinate(self, coordinate: Coordinates) -> Shape:
        k = {value: key for key, value in enumerate(HorizontalCoordinates)}
        return self[coordinate.vertical][k[coordinate.horizontal]].shape

    def change_square_shape(self, coordinate: Coordinates, new_shape: Shape):
        k = {value: key for key, value in enumerate(HorizontalCoordinates)}
        self[coordinate.vertical][k[coordinate.horizontal]].shape = new_shape

    def rm_shape_from_square(self, coordinate: Coordinates):
        k = {value: key for key, value in enumerate(HorizontalCoordinates)}
        self[coordinate.vertical][k[coordinate.horizontal]].rm_shape()

    def get_shape_moves(self, coordinates: Coordinates) -> List[Coordinates]:
        if self.is_have_shape_by_coordinate(coordinates):
            shape = self.get_shape_by_coordinate(coordinates)
            return shape.get_available_moves()

    def move(self, _from: Coordinates, to: Coordinates):
        if self.is_have_shape_by_coordinate(_from):
            my_shape = self.get_shape_by_coordinate(_from)
            self.change_square_shape(to, my_shape)
            self.rm_shape_from_square(_from)

    def __repr__(self):
        output = ""

        for num, row in zip(list(VerticalCoordinates)[::-1], self[::-1]):
            output += f"{num}  " + "".join([f"{square}" for square in row])
            output += "\n"
        output += "    " + "  ".join(HorizontalCoordinates)

        return output
