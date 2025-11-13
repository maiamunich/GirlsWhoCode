def make_boolean_square_board(n):
    """
    Makes a 2D board of a desired size filled with False as default value.

    Args:
        n (int): size of the board.

    Returns:
        list[list[bool]]: board of desired size.
    """
    board = []

    for i in range(n):
        x = []
        for j in range(n):
            x.append(False)  # add n False elements to a row
        board.append(x)  # add filled row to the board
    return board
