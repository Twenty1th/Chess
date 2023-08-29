from coordinate import Coordinate


class MovesFilter:

    @staticmethod
    def filters():
        filters = {
            'TOP': MovesFilter.top_filter,
            'DOWN': MovesFilter.down_filter,
            'RIGHT': MovesFilter.right_filter,
            'LEFT': MovesFilter.left_filter,
            'TOP_RIGHT': MovesFilter.top_right_filter,
            'TOP_LEFT': MovesFilter.top_left_filter,
            'DOWN_RIGHT': MovesFilter.down_right_filter,
            'DOWN_LEFT': MovesFilter.down_left_filter,
            'JUMP': MovesFilter.jump
        }
        return filters

    @staticmethod
    def filter(board, shape):
        filtered_moves = []
        for direction in shape.direction_options:
            for move in MovesFilter.filters().get(direction)(shape):
                coordinate = Coordinate(move.horizontal, move.vertical)
                if not board.is_have_shape_by_coordinate(coordinate):
                    filtered_moves.append(move)
                else:
                    if board.get_shape_by_coordinate(coordinate).color != shape.color:
                        filtered_moves.append(move)
                    elif board.get_shape_by_coordinate(coordinate).color == shape.color:
                        if direction != "JUMP":
                            break

        return filtered_moves

    @staticmethod
    def top_filter(shape):
        return sorted([move for move in shape.get_available_coordinates_to_move()
                       if move.horizontal == shape.coordinate.horizontal
                       and
                       move.vertical > shape.coordinate.vertical],
                      key=lambda x: x.vertical)

    @staticmethod
    def down_filter(shape):
        return sorted([move for move in shape.get_available_coordinates_to_move()
                       if move.horizontal == shape.coordinate.horizontal
                       and
                       move.vertical < shape.coordinate.vertical],
                      key=lambda x: x.vertical)[::-1]

    @staticmethod
    def top_right_filter(shape):
        return sorted([move for move in shape.get_available_coordinates_to_move()
                       if move.horizontal > shape.coordinate.horizontal
                       and
                       move.vertical > shape.coordinate.vertical],
                      key=lambda x: x.vertical)

    @staticmethod
    def top_left_filter(shape):
        return sorted([move for move in shape.get_available_coordinates_to_move()
                       if move.horizontal < shape.coordinate.horizontal
                       and
                       move.vertical > shape.coordinate.vertical],
                      key=lambda x: x.horizontal)[::-1]

    @staticmethod
    def down_right_filter(shape):
        return sorted([move for move in shape.get_available_coordinates_to_move()
                       if move.horizontal > shape.coordinate.horizontal
                       and
                       move.vertical < shape.coordinate.vertical],
                      key=lambda x: x.horizontal)

    @staticmethod
    def down_left_filter(shape):
        return sorted([move for move in shape.get_available_coordinates_to_move()
                       if move.horizontal < shape.coordinate.horizontal
                       and
                       move.vertical < shape.coordinate.vertical],
                      key=lambda x: x.horizontal)[::-1]

    @staticmethod
    def left_filter(shape):
        return sorted([move for move in shape.get_available_coordinates_to_move()
                       if move.vertical == shape.coordinate.vertical
                       and
                       move.horizontal < shape.coordinate.horizontal],
                      key=lambda x: x.horizontal)[::-1]

    @staticmethod
    def right_filter(shape):
        return sorted([move for move in shape.get_available_coordinates_to_move()
                       if move.vertical == shape.coordinate.vertical
                       and
                       move.horizontal > shape.coordinate.horizontal],
                      key=lambda x: x.vertical)

    @staticmethod
    def jump(shape):
        return shape.get_available_coordinates_to_move()
