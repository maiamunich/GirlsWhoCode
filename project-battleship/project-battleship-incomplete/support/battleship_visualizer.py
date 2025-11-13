"""
Visualization functions for an implementation of the battleship game.
"""

from .battleship_helpers import *


BLUE = "\033[34m"
GREEN = "\033[32m"
RED = "\033[31m"
DEFAULT = "\033[0m"
CELL_WIDTH_WITH_BORDERS = 6
CELL_WIDTH = 4


def print_board_header(board):
    """
    Print the header of the board, showing the column numbers.
     
    Args:
        board (list[list[bool]]): 2D list representing player's ship board.
    """
    print('\n       ' + '     '.join([str(i+1) for i in range(len(board))]))


def make_visual_ship_board(board):
    """
    Create visual representation of ship board.
     
    Args:
        board (list[list[bool]]): 2D list representing player's ship board. 
        False represents an empty space, and True represents a ship.

    Returns:
        (list[list[str]]): 2D list representing the visual state of the board.
    """
    visual_board = []
    for i in range(len(board)):
        visual_board.append([])
        for j in range(len(board)):
            if not board[i][j]:
                visual_board[i].append(' ')
            else:
                visual_board[i].append(f"{BLUE}S{DEFAULT}")
    return visual_board


def print_board_rows(visual_board):
    """
    Print the rows of the board based on the visual representation.
     
    Args:
        visual_board (list[list[str]]): 2D list representing the visual state 
        of the board.
    """
    for i in range(len(visual_board)):
        print(CELL_WIDTH*' ' + '-' * (CELL_WIDTH_WITH_BORDERS*len(visual_board)+1))
        print(f"  {i+1} |  {'  |  '.join(visual_board[i])}  |")
    print(CELL_WIDTH*' ' + '-' * (CELL_WIDTH_WITH_BORDERS*len(visual_board)+1) + '\n')


def visualize_ship_board(board):
    """
    Display the current player's ship board.
     
    Args:
        board (list[list[bool]]): 2D list representing player's ship board. 
        False represents an empty space, and True represents a ship.
    """
    print_board_header(board)
    visual_board = make_visual_ship_board(board)
    print_board_rows(visual_board)


def get_sunk_ships(ships, board_hits, player):
    """
    Determine which ships have been sunk based on the hits received.
     
    Args:
        ships (list[list[tuple[int, int]]]): ships' coordinates.
        board_hits (list[list[list[bool]]]): players' hit boards.
        player (int): index of player (0 for Player 1, 1 for Player 2).

    Returns:
        (list[tuple[int, int]]): coordinates of sunk ships.
    """
    sunk_ships = []
    for ship in ships:
        sunk = True
        for coord in ship:
            if board_hits[player][coord[1]][coord[0]] == 0:
                sunk = False
                break
        if sunk:
            sunk_ships.extend(ship)
    return sunk_ships


def make_visual_playing_board(board_ships, board_hits, sunk_ships, player, board_no):
    """
    Create a visual representation of the game board for display.
     
    Args:
        board_ships (list[list[list[bool]]]): players' ship boards. 
        False indicates no ship, and True indicates a ship.
        board_hits (list[list[list[bool]]]): players' hit boards. 
        False indicates no hit, and True indicates a hit.
        sunk_ships (list[tuple[int, int]]): coordinates of sunk ships.
        player (int): index of player (0 for Player 1, 1 for Player 2).
        board_no (int): index of board to visualize (0 for opponent's board 
        without ships, 1 for opponent's board with ship visibility)

    Returns:
        (list[list[str]]): visual state of the board.
    """
    visual_board = []
    for i in range(len(board_ships[player])):
        visual_board.append([])
        for j in range(len(board_ships[player])):
            if not board_ships[get_opponent(player)][i][j] and \
                not board_hits[player][i][j]:
                visual_board[i].append(' ')
            elif not board_ships[get_opponent(player)][i][j] and \
                board_hits[player][i][j]:
                visual_board[i].append('*')
            elif board_ships[get_opponent(player)][i][j] and \
                not board_hits[player][i][j] and board_no == 0:
                visual_board[i].append(' ')
            elif board_ships[get_opponent(player)][i][j] and \
                not board_hits[player][i][j]:
                visual_board[i].append(f"{BLUE}S{DEFAULT}")
            elif (j, i) in sunk_ships:
                visual_board[i].append(f"{RED}*{DEFAULT}")
            else:
                visual_board[i].append(f"{GREEN}*{DEFAULT}")
    return visual_board


def visualize_boards(board_ships, board_hits, player, ships):
    """
    Display a visualization of the current player's ship board and hit boards.
     
    Args:
        board_ships (list[list[list[bool]]]): players' ship boards. 
        False indicates no ship, and True indicates a ship.
        board_hits (list[list[list[bool]]]): players' hit boards. 
        False indicates no hit, and True indicates a hit.
        player (int): index of player (0 for Player 1, 1 for Player 2).
        ships (list[list[tuple[int, int]]]): ships' coordinates.
    """
    for x in range(2):
        print_board_header(board_ships[player])
        sunk_ships = get_sunk_ships(ships, board_hits, player)
        visual_board = make_visual_playing_board(board_ships, board_hits, sunk_ships, player, x)
        print_board_rows(visual_board)

        if x == 0:
            print('=' * (CELL_WIDTH_WITH_BORDERS*(len(board_ships[player])+1)+1))
            player = get_opponent(player)
