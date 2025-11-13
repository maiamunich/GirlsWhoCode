from src.task1 import get_opponent


def check_win(board_ships, board_hits, player, size_board):
    """
    Check if the current player has won by hitting all of the opponent's ships.

    Args:
        board_ships (list[list[list[bool]]]): players' ship boards.
        board_hits (list[list[list[bool]]]): players' hit boards.
        player (int): current player (0 for Player 1, 1 for Player 2).
        size_board (int): size of the board.

    Returns:
        bool: True if player has won, False otherwise.
    """

    board_ship_opp = board_ships[get_opponent(player)]
    board_hits_player = board_hits[player]

    for i in range(len(board_ship_opp)):  # loop through rows
        for j in range(len(board_ship_opp[i])):  # loop through columns
            # if a ship at spot i, j and it hasnt been hit return False
            if board_ship_opp[i][j] and not board_hits_player[i][j]:
                return False
    return True
