from dataclasses import dataclass

from enums import HorizontalCoordinates


@dataclass
class Coordinate:
    horizontal: str
    vertical: int

    def __init__(self, horizontal: str, vertical: int):
        self.horizontal = horizontal
        self.vertical = vertical

    def __lt__(self, other: 'Coordinate'):
        k = {value.value: key for key, value in enumerate(HorizontalCoordinates)}
        return k[self.horizontal] + self.vertical < k[other.horizontal] + other.vertical

    def __gt__(self, other):
        k = {value.value: key for key, value in enumerate(HorizontalCoordinates)}
        return k[self.horizontal] + self.vertical > k[other.horizontal] + other.vertical

    def __eq__(self, other):
        k = {value.value: key for key, value in enumerate(HorizontalCoordinates)}
        return self.horizontal == other.horizontal and self.vertical == other.vertical

    def __repr__(self):
        return f"{self.horizontal}{self.vertical}"
