from enum import StrEnum, IntEnum
from typing import Dict

from colorama import Fore


class HorizontalCoordinates(StrEnum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"

    @classmethod
    def get_index(cls, item) -> int:
        return cls.items()[item]

    @classmethod
    def items(cls) -> Dict:
        k = {value: key for key, value in enumerate(HorizontalCoordinates)}
        return k


class VerticalCoordinates(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8


class ShapeUnicodes(StrEnum):
    KING = "\u2654"
    QUEEN = "\u2655"
    ROOK = "\u2656"
    BISHOP = "\u2657"
    KNIGHT = "\u2658"
    PAWN = "\u2659"


class ShapeColors(StrEnum):
    BLACK = Fore.LIGHTBLACK_EX
    WHITE = Fore.BLUE
