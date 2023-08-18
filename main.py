from board import Board
from coordinates import Coordinates

if __name__ == '__main__':
    board = Board()
    coordinate = Coordinates("G", 1)
    new_coord = board.get_shape_moves(coordinate)
    print(new_coord)
    board.move(coordinate, new_coord[1])
    print(board)


