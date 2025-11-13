def get_opponent(player):
    """
    Find the opponent of the current player

    Args:
        player(0,1): player number

    Returns:
        0 and 1 depending on which player is playing. 
        Returns -1 if wrong number is detected
    """
    # Check if the player number is valid
    if player == 0:  # the return is the opponent of the player
        return 1
    elif player == 1:
        return 0
    else:
        # print("Incorrect player detected")
        return -1
