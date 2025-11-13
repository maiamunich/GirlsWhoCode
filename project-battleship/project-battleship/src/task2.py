def check_valid_coord(coord, board):
    """
    Check whether the coordinates are valid on a board.

    Args:
        coord (tuple[int, int]): coordinates.
        board (list[list[bool]]): ship or hit board.

    Returns:
        bool: True if the coordinates are valid, False otherwise.
    """
    x = coord[0]
    y = coord[1]

    if board == []:  # checking to see if board is empty, if it is gives False
        return False

    if board[0] == []:  # checking to see if first row is empty, if it is gives False
        return False

    # x max will be the length of the first item in the board list
    xmax = len(board[0])
    ymax = len(board)  # y max will be the length of the whole board

    # check to see if both coordinates are within the board
    return 0 <= x < xmax and 0 <= y < ymax
