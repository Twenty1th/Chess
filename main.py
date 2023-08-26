from board import Board
from coordinates import Coordinates

if __name__ == '__main__':
    board = Board()
    print(board)

    pawn = board.get_shape_by_coordinate(Coordinates("A", 2))
    board.move(pawn, board.get_shape_moves(pawn)[1])
    print(board)

    pawn = board.get_shape_by_coordinate(Coordinates("B", 2))
    board.move(pawn, board.get_shape_moves(pawn)[1])
    print(board)

    bishop = board.get_shape_by_coordinate(Coordinates("C", 1))
    bishop_moves = board.get_shape_moves(bishop)
    board.move(bishop, bishop_moves[1])
    print(board)

    bishop = board.get_shape_by_coordinate(Coordinates("B", 2))
    bishop_moves = board.get_shape_moves(bishop)
    print(bishop_moves)
    board.move(bishop, bishop_moves[1])
    print(board)

    # coordinates = Coordinates("A", 1)
    # rook = board.get_shape_by_coordinate(coordinates)
    # rook_moves = board.get_shape_moves(rook)
    # board.move(rook, rook_moves[1])
    # print(board)
    #
    # coordinates = Coordinates("A", 3)
    # rook = board.get_shape_by_coordinate(coordinates)
    # rook_moves = board.get_shape_moves(rook)
    # board.move(rook, rook_moves[-1])
    # print(board)
    #
    # coordinates = Coordinates("H", 3)
    # rook = board.get_shape_by_coordinate(coordinates)
    # rook_moves = board.get_shape_moves(rook)
    # board.move(rook, rook_moves[4])
    #
    # coordinates = Coordinates("B", 1)
    # knight = board.get_shape_by_coordinate(coordinates)
    # knight_moves = board.get_shape_moves(knight)
    # print(knight_moves)
    # board.move(knight, knight_moves[1])
    # print(board)
