from collections import namedtuple

from coordinates import Coordinates
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
    def __calculate_params(cls, coordinates: Coordinates) -> Knight | None:
        match coordinates:
            case Coordinates(_, 2):
                _unicode_symbol = ShapeUnicodes.PAWN
                _color = ShapeColors.WHITE
                _shape = Pawn

            case Coordinates(_, 7):
                _unicode_symbol = ShapeUnicodes.PAWN
                _color = ShapeColors.BLACK
                _shape = Pawn

            case Coordinates("A", 1) | Coordinates("H", 1):
                _unicode_symbol = ShapeUnicodes.ROOK
                _color = ShapeColors.WHITE
                _shape = Rook

            case Coordinates("A", 8) | Coordinates("H", 8):
                _unicode_symbol = ShapeUnicodes.ROOK
                _color = ShapeColors.BLACK
                _shape = Rook

            case Coordinates("B", 1) | Coordinates("G", 1):
                _unicode_symbol = ShapeUnicodes.KNIGHT
                _color = ShapeColors.WHITE
                _shape = Knight

            case Coordinates("B", 8) | Coordinates("G", 8):
                _unicode_symbol = ShapeUnicodes.KNIGHT
                _color = ShapeColors.BLACK
                _shape = Knight

            case Coordinates("C", 1) | Coordinates("F", 1):
                _unicode_symbol = ShapeUnicodes.BISHOP
                _color = ShapeColors.WHITE
                _shape = Bishop

            case Coordinates("C", 8) | Coordinates("F", 8):
                _unicode_symbol = ShapeUnicodes.BISHOP
                _color = ShapeColors.BLACK
                _shape = Bishop

            case Coordinates("D", 1):
                _unicode_symbol = ShapeUnicodes.KING
                _color = ShapeColors.WHITE
                _shape = King

            case Coordinates("D", 8):
                _unicode_symbol = ShapeUnicodes.KING
                _color = ShapeColors.BLACK
                _shape = King

            case Coordinates("E", 1):
                _unicode_symbol = ShapeUnicodes.QUEEN
                _color = ShapeColors.WHITE
                _shape = Queen

            case Coordinates("E", 8):
                _unicode_symbol = ShapeUnicodes.QUEEN
                _color = ShapeColors.BLACK
                _shape = Queen

            case _:
                return None

        return _shape(coordinates=coordinates, color=_color, unicode=_unicode_symbol)

    @classmethod
    def get_shape_by_coordinates(cls, coordinates: Coordinates) -> Shape | None:
        shape = cls.__calculate_params(coordinates=coordinates)
        return shape
