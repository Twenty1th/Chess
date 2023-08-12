from coordinates import Coordinates
from enums import VerticalCoordinates, HorizontalCoordinates
from colorama import Fore, Back, Style


if __name__ == '__main__':
    # c = Coordinates(vertical=VerticalCoordinates.ONE, horizontal=HorizontalCoordinates.A)
    # print(Back.BLACK + "  " + Back.WHITE + "  " + Style.RESET_ALL)
    print(list(VerticalCoordinates).index(1))