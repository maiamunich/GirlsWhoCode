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
            # split the user input into a list of two strings, one for the x coordinate and one for the y coordinate
            

            # check if the x and y coordinates are digits


                # making these values the correct index value (one less than original)
                


                if check_valid_coord((x, y), board) and not board[y][x]:
                    need_to_check = False
                else:
                    print(VALID)
            else:
                print(TWO_NUMS)
        else:
            print(INVALID)
    return x, y
