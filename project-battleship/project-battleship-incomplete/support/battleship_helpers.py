"""
Helper functions for an implementation of the battleship game.
"""

from src.task1 import get_opponent
from src.task2 import check_valid_coord


PURPLE = "\033[35m"
DEFAULT = "\033[0m"
RULES = """
Here are the rules of the game:

 - This is a 2 player game, have someone to play with you!
 - Each ship is positioned using its upper-left coordinate!
 - You must sink all of your opponent's ships before they sink yours!

Enjoy the game!
"""


def check_placement(ship_board, ship, coord, rotate):
    """
    Check whether a ship can be placed on a board at a certain coordinate 
    location based on the constraints of the battleship game.
    
    Args:
        ship_board (list[list[bool]]): ship board.
        ship (int): length of the ship.
        coord (tuple[int, int]): coordinates
        rotate (bool): True if ship is vertical, False if horizontal.
    
    Returns:
        bool: True if the ship can be placed, False otherwise.
    """
    x, y = coord
    for i in range(ship):
        if rotate:
            if not check_valid_coord((y+i, x), ship_board) or ship_board[y+i][x]:
                return False
        else:
            if not check_valid_coord((y, x+i), ship_board) or ship_board[y][x+i]:
                return False
    return True


def switch_player(player, rounds):
    """
    Switches between player 1 and 2 in the game of battleship with 
    instructions for the players. 
    Arguments: none
    """
    input(f"Player {player + 1}, press Enter to clear the terminal and pass \
the computer to the other player!")
    clear()
    print(f"{PURPLE}Player {get_opponent(player) + 1} - Round {rounds}{DEFAULT}\n")
    input(f"Player {get_opponent(player) + 1}, ready to start your turn? Press Enter to \
continue!")
    return get_opponent(player)
    

def clear():
    """
    Clears the terminal screen.
    """
    print("\033c", end="", flush=True)