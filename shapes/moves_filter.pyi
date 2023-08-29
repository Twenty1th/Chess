from typing import List, Callable, Dict

from board import Board
from coordinate import Coordinate
from shapes.shape import Shape


class MovesFilter:
    @staticmethod
    def filters() -> Dict[str, Callable[[Shape], List[Coordinate]]]:
        ...

    @staticmethod
    def filter(board: Board, shape: Shape) -> List[Coordinate]:
        ...

    @staticmethod
    def top_filter(shape: Shape):
        ...

    @staticmethod
    def down_filter(shape: Shape):
        ...

    @staticmethod
    def top_right_filter(shape: Shape):
        ...

    @staticmethod
    def top_left_filter(shape: Shape):
        ...

    @staticmethod
    def down_right_filter(shape: Shape):
        ...

    @staticmethod
    def down_left_filter(shape: Shape):
        ...

    @staticmethod
    def left_filter(shape: Shape):
        ...

    @staticmethod
    def right_filter(shape: Shape):
        ...

    @staticmethod
    def jump(shape: Shape):
        ...