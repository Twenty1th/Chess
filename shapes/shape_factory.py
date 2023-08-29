from collections import namedtuple

from coordinate import Coordinate
from enums import ShapeUnicodes, ShapeColors
from shapes.bishop import Bishop
from shapes.king import King
from shapes.knight import Knight
from shapes.pawn import Pawn
from shapes.queen import Queen
from shapes.rook import Rook
from shapes.shape import Shape


class ShapeFactory:

    @classmethod
    def __calculate_params(cls, coordinates: Coordinate) -> Knight | None:
        match coordinates:
            case Coordinate(_, 2):
                _unicode_symbol = ShapeUnicodes.PAWN
                _color = ShapeColors.WHITE
                _shape = Pawn

            case Coordinate(_, 7):
                _unicode_symbol = ShapeUnicodes.PAWN
                _color = ShapeColors.BLACK
                _shape = Pawn

            case Coordinate("A", 1) | Coordinate("H", 1):
                _unicode_symbol = ShapeUnicodes.ROOK
                _color = ShapeColors.WHITE
                _shape = Rook

            case Coordinate("A", 8) | Coordinate("H", 8):
                _unicode_symbol = ShapeUnicodes.ROOK
                _color = ShapeColors.BLACK
                _shape = Rook

            case Coordinate("B", 1) | Coordinate("G", 1):
                _unicode_symbol = ShapeUnicodes.KNIGHT
                _color = ShapeColors.WHITE
                _shape = Knight

            case Coordinate("B", 8) | Coordinate("G", 8):
                _unicode_symbol = ShapeUnicodes.KNIGHT
                _color = ShapeColors.BLACK
                _shape = Knight

            case Coordinate("C", 1) | Coordinate("F", 1):
                _unicode_symbol = ShapeUnicodes.BISHOP
                _color = ShapeColors.WHITE
                _shape = Bishop

            case Coordinate("C", 8) | Coordinate("F", 8):
                _unicode_symbol = ShapeUnicodes.BISHOP
                _color = ShapeColors.BLACK
                _shape = Bishop

            case Coordinate("E", 1):
                _unicode_symbol = ShapeUnicodes.KING
                _color = ShapeColors.WHITE
                _shape = King

            case Coordinate("E", 8):
                _unicode_symbol = ShapeUnicodes.KING
                _color = ShapeColors.BLACK
                _shape = King

            case Coordinate("D", 1):
                _unicode_symbol = ShapeUnicodes.QUEEN
                _color = ShapeColors.WHITE
                _shape = Queen

            case Coordinate("D", 8):
                _unicode_symbol = ShapeUnicodes.QUEEN
                _color = ShapeColors.BLACK
                _shape = Queen

            case _:
                return None

        return _shape(coordinates=coordinates, color=_color, unicode=_unicode_symbol)

    @classmethod
    def get_shape_by_coordinates(cls, coordinates: Coordinate) -> Shape | None:
        shape = cls.__calculate_params(coordinates=coordinates)
        return shape
