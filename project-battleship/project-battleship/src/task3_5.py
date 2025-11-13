from src.task2 import check_valid_coord

PROMPT = 'Enter the desired coordinates x,y: '
VALID = 'Make sure that the location is valid!'
TWO_NUMS = 'Your coordinates must be 2 numbers!'
INVALID = 'Your coordinates format is invalid! Please enter as x,y.'


def ask_coordinates(board):
    """
    Ask the player for valid coordinates on a board in an x,y format.

    Args:
        board (list[list[bool]]): ship or hit board. 
        False represents an empty space, and True represents a ship or hit.

    Returns:
        tuple[int, int]: valid x and y coordinates.
    """
    need_to_check = True
    # Until all conditions have been fulfilled, the user is asked to input new
    # coordinates as the previous ones were not valid. The variable
    # need_to_check is initially set to True and set to False once all of the
    # conditions have been fulfilled, to exit the while loop.
    while need_to_check:
        user_input = input(PROMPT)
        if ',' in user_input:
            coordinates = user_input.split(',')

            if len(coordinates) == 2 and coordinates[0].isdigit() and coordinates[1].isdigit():
                # making these values the correct index value (one less than original)
                x = int(coordinates[0]) - 1
                # making these values the correct index value (one less than original)
                y = int(coordinates[1]) - 1

                if check_valid_coord((x, y), board) and not board[y][x]:
                    need_to_check = False
                else:
                    print(VALID)
            else:
                print(TWO_NUMS)
        else:
            print(INVALID)
    return x, y
