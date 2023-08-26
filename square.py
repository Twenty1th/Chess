from colorama import Back, Style

from coordinates import Coordinates
from shapes.shape import Shape


class Square:

    def __init__(self,  shape: Shape, coordinates: Coordinates):
        self._coordinates: Coordinates = coordinates
        self._DEFAULT_BACKGROUND_COLOR: Back = Back.BLACK if (ord(self._coordinates.horizontal) + self._coordinates.vertical) % 2 == 0 else Back.WHITE
        self._background_color: Back = self._DEFAULT_BACKGROUND_COLOR
        self._shape: Shape = shape

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, value: Shape):
        self._shape = value

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def background_color(self):
        return self.background_color

    @background_color.setter
    def background_color(self, value: str):
        self._background_color = value

    @property
    def default_background_color(self):
        return self._DEFAULT_BACKGROUND_COLOR

    def rm_shape(self):
        self._shape = None

    def reset_background_color(self):
        self._background_color = self._DEFAULT_BACKGROUND_COLOR

    def __repr__(self):
        return self._background_color + f"{self._shape if self.shape else '   '}" + Style.RESET_ALL
