def go_to_next_round(player, round):
    """
    Returns the round value once the current player has finished their turn.

    Args:
        player (int): current player (0 for Player 1, 1 for Player 2).
        round (int): current round number.

    Returns:
        int: new round value.
    """

    # when current player is done the round count increases
