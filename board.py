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
        new_shape.coordinates = coordinate
        self[coordinate.vertical][k[coordinate.horizontal]].shape = new_shape

    def rm_shape_from_square(self, shape: Shape):
        k = {value: key for key, value in enumerate(HorizontalCoordinates)}
        self[shape.coordinates.vertical][k[shape.coordinates.horizontal]].rm_shape()

    def get_shape_moves(self, shape: Shape) -> List[Coordinates]:  # noqa
        moves: List[Coordinates] = []
        min_horiz_coord: str = "A"
        max_horiz_coord: str = "H"
        min_vertical_coord: int = 1
        max_vertical_coord: int = 7
        for coordinate in shape.get_available_moves():
            if not self.coordinate_is_available(coordinate):
                if coordinate.vertical > shape.coordinates.vertical and not coordinate.vertical > max_vertical_coord:
                    max_vertical_coord = coordinate.vertical
                elif coordinate.vertical < shape.coordinates.vertical and not coordinate.vertical < min_vertical_coord:
                    min_vertical_coord = coordinate.vertical
                if coordinate.horizontal > shape.coordinates.horizontal and not coordinate.horizontal > max_horiz_coord:
                    max_horiz_coord = coordinate.horizontal
                elif coordinate.horizontal < shape.coordinates.horizontal and not coordinate.horizontal < min_horiz_coord:
                    min_horiz_coord = coordinate.horizontal
            else:
                if any(
                        [(
                                coordinate.vertical >= shape.coordinates.vertical
                                and not
                                coordinate.vertical > max_vertical_coord
                                and
                                coordinate.horizontal >= shape.coordinates.horizontal
                                and not
                                coordinate.horizontal > max_horiz_coord
                        ),
                        (
                                coordinate.vertical <= shape.coordinates.vertical
                                and not
                                coordinate.vertical < min_vertical_coord
                                and
                                coordinate.horizontal <= shape.coordinates.horizontal
                                and not
                                coordinate.horizontal < min_horiz_coord),
                        (
                                coordinate.vertical >= shape.coordinates.vertical
                                and not
                                coordinate.vertical > max_vertical_coord
                                and
                                coordinate.horizontal <= shape.coordinates.horizontal
                                and
                                coordinate.horizontal < max_horiz_coord
                        ),
                        (
                                coordinate.vertical <= shape.coordinates.vertical
                                and not
                                coordinate.vertical < min_vertical_coord
                                and
                                coordinate.horizontal >= shape.coordinates.horizontal
                                and not
                                coordinate.horizontal > min_horiz_coord
                        ),
                        shape.can_jump
                        ]
                        ):
                    moves.append(coordinate)
        print(min_horiz_coord, max_horiz_coord, min_vertical_coord, max_vertical_coord)
        return moves

    def coordinate_is_available(self, coordinate: Coordinates):
        k = {value: key for key, value in enumerate(HorizontalCoordinates)}
        return self[coordinate.vertical][k[coordinate.horizontal]].shape is None

    def move(self, shape: Shape, to: Coordinates):
        self.rm_shape_from_square(shape)
        self.change_square_shape(to, shape)

    def __repr__(self):
        output = ""

        for num, row in zip(list(VerticalCoordinates)[::-1], self[::-1]):
            output += f"{num}  " + "".join([f"{square}" for square in row])
            output += "\n"
        output += "    " + "  ".join(HorizontalCoordinates)

        return output
