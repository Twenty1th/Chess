from typing import List

from shapes.shape import Shape
from shapes.shape_factory import ShapeFactory
from square import Square
from coordinates import Coordinates
from enums import HorizontalCoordinates, VerticalCoordinates

board = List[List[Square]]


class Board(board):

    def __init__(self):
        super().__init__()
        rows = [[Square(coordinates=Coordinates(horizontal, vertical),
                        shape=ShapeFactory.get_shape_by_coordinates(coordinates=Coordinates(horizontal, vertical)))
                 for horizontal in HorizontalCoordinates]
                for vertical in VerticalCoordinates]
        self.extend(rows)

    def __getitem__(self, item: int | slice):
        if isinstance(item, int):
            adjusted_index = item - 1
            if 0 <= adjusted_index < len(self):
                return super().__getitem__(adjusted_index)
            else:
                raise IndexError("Index out of range")
        return super().__getitem__(item)

    def is_have_shape_by_coordinate(self, coordinate: Coordinates) -> bool:
        return self[coordinate.vertical][HorizontalCoordinates.get_index(coordinate.horizontal)].shape is not None

    def get_shape_by_coordinate(self, coordinate: Coordinates) -> Shape:
        return self[coordinate.vertical][HorizontalCoordinates.get_index(coordinate.horizontal)].shape

    def change_square_shape(self, coordinate: Coordinates, new_shape: Shape):
        new_shape.coordinates = coordinate
        self[coordinate.vertical][HorizontalCoordinates.get_index(coordinate.horizontal)].shape = new_shape

    def rm_shape_from_square(self, shape: Shape):
        self[shape.coordinates.vertical][HorizontalCoordinates.get_index(shape.coordinates.horizontal)].rm_shape()

    def get_shape_moves(self, shape: Shape) -> List[Coordinates]:  # noqa
        moves: List[Coordinates] = []
        min_horiz_coord: str = ""
        max_horiz_coord: str = "I"
        min_vertical_coord: int = 0
        max_vertical_coord: int = 8
        for coordinate in sorted(shape.get_available_moves(), key=lambda x: x.horizontal):
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
                        [
                            # Top / Down
                            (
                                    shape.coordinates.horizontal == coordinate.horizontal
                                    and
                                    shape.coordinates.vertical < coordinate.vertical < max_vertical_coord
                            ),
                            (
                                    shape.coordinates.horizontal == coordinate.horizontal
                                    and
                                    min_vertical_coord < coordinate.vertical < shape.coordinates.vertical
                            ),
                            (
                                    shape.coordinates.vertical >= coordinate.vertical > min_vertical_coord
                                    and
                                    shape.coordinates.horizontal >= coordinate.horizontal > min_horiz_coord),

                            # Left / Right

                            (
                                    shape.coordinates.vertical == coordinate.vertical
                                    and
                                    min_horiz_coord < coordinate.horizontal <= shape.coordinates.horizontal
                            ),
                            (
                                    shape.coordinates.vertical == coordinate.vertical
                                    and
                                    max_horiz_coord > coordinate.horizontal >= shape.coordinates.horizontal
                            ),

                            # Horizontal
                            (
                                    shape.coordinates.vertical < coordinate.vertical < max_vertical_coord
                                    or
                                    min_horiz_coord < coordinate.horizontal < shape.coordinates.horizontal
                            ),
                            (
                                    shape.coordinates.vertical < coordinate.vertical < max_vertical_coord
                                    or
                                    shape.coordinates.horizontal < coordinate.horizontal < max_horiz_coord
                            ),
                            (
                                    min_vertical_coord < coordinate.vertical < shape.coordinates.vertical
                                    or
                                    min_horiz_coord < coordinate.horizontal < shape.coordinates.horizontal
                            ),
                            (
                                    shape.coordinates.vertical < coordinate.vertical < max_vertical_coord
                                    or
                                    shape.coordinates.horizontal < coordinate.horizontal < max_horiz_coord
                            ),
                            shape.can_jump
                        ]
                ):
                    moves.append(coordinate)
        return moves

    def coordinate_is_available(self, coordinate: Coordinates):
        return self[coordinate.vertical][HorizontalCoordinates.get_index(coordinate.horizontal)].shape is None

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
