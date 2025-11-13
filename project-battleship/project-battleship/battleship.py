"""
Main game loop of a battleship game implementation.
"""

from support.battleship_helpers import *
from support.battleship_visualizer import *
from src.task3_5 import ask_coordinates
from src.task6 import make_boolean_square_board
from src.task11 import check_win
from src.task12 import go_to_next_round

# Define constants and variables
# no ship of length 0 or 1, 2 ships of length 2, 2 of length 3, and 1 of 4
SHIPS = [0, 0, 2, 2, 1]
PURPLE = "\033[35m"
DEFAULT = "\033[0m"
N = 7

WELCOME_MSG = "Welcome to Battleships, the 2 player version!"
PLAYER_1_PROMPT = "Player 1, when you are ready to start the game, hide the screen from your opponent and press Enter!"


def round_message(player, rounds):
    """
    Creates a message to headline the round.

    Args:
        player (int): The current player (0 for Player 1, 1 for Player 2).
        rounds (int): The current round number.
    """
    return PURPLE + "Player " + str(player) + " - Round " + str(rounds) + DEFAULT + "\n"

# Intro message to players


def intro(player, rounds):
    """
    Display an introduction message to the players and begin the game.

    Args:
        player (int): The current player (0 for Player 1, 1 for Player 2).
        rounds (int): The current round number.
    """
    clear()
    print(WELCOME_MSG)
    print(RULES)
    input(PLAYER_1_PROMPT)
    clear()
    print(round_message(player + 1, rounds))


ROTATE_MSG = "Do you want to rotate the ship from horizontal to vertical? "
INVALID_POSITION_MSG = "Invalid position for your ship, try again!"
YES = 'Y'


def place_ships(player, rounds, board_ships_p, ships_placed):
    """
    Allow a player to place their ships on the board.

    Args:
        player (int): current player (0 for Player 1, 1 for Player 2).
        rounds (int): current round number.
        board_ships_p (list[list[bool]]): player's ship board.
        ships_placed (list[list[tuple[int, int]]]): coords of placed ships.
    """
    # Players need to place their ships
    visualize_ship_board(board_ships_p)
    for length in range(len(SHIPS) - 1, 0, -1):
        for i in range(SHIPS[length]):
            print("Place a ship of size " + str(length) + "!")

            invalid_placement = True
            rotate = False
            while invalid_placement:
                # Checks valid coordinate
                coord = ask_coordinates(board_ships_p)
                # Rotate ship for player if desired
                if input(ROTATE_MSG).upper() == YES:
                    rotate = True
                if not check_placement(board_ships_p, length, coord, rotate):
                    print(INVALID_POSITION_MSG)
                else:
                    invalid_placement = False

            x = coord[0]
            y = coord[1]
            new_ship = []

            for j in range(length):
                if rotate:  # will rotate with the given numbers
                    board_ships_p[y + j][x] = True
                    new_ship.append((x, y + j))
                else:  # wont rotate and will just put numbers into new_ship
                    board_ships_p[y][x + j] = True
                    new_ship.append((x + j, y))

            # player gives 0 or 1 which is also the index of the list we will append from
            ships_placed[player].append(new_ship)

            clear()
            print(round_message(player + 1, rounds))
            visualize_ship_board(board_ships_p)


def congrats_message(player, rounds):
    """
    Creates a message to congratulate the winner.

    Args:
        player (int): The current player (0 for Player 1, 1 for Player 2).
        rounds (int): The current round number.
    """

    return "Congratulations Player " + str(player) + "! You sank all of the enemy ships in " + str(rounds) + " rounds!"


CAREFUL_MSG = "You're on the offensive, choose your next spot carefully!"
HIT_MSG = "And that's a hit! Woohoo! Your turn again!"
MISS_MSG = "You missed, better luck next time..."


def attack(player, rounds, board_ships, board_hits, ships_placed):
    """
    Allow a player to attack the opponent's ships.

    Args:
        player (int): current player (0 for Player 1, 1 for Player 2).
        rounds (int): current round number.
        board_ships (list[list[list[bool]]]): players' ship boards.
        board_hits (list[list[list[bool]]]): players' hit boards.
        ships_placed (list[list[tuple[int, int]]]): coords of placed ships.

    Returns:
        bool: True if the attack was a miss, False otherwise.
    """
    print(CAREFUL_MSG)
    coords = ask_coordinates(board_hits[player])
    x = coords[0]
    y = coords[1]
    opp = get_opponent(player)
    board_hits[player][y][x] = True
    if board_ships[opp][y][x]:
        # Check if player won!
        if check_win(board_ships, board_hits, player, N):
            clear()
            print(congrats_message(player + 1, rounds))
            exit()
        clear()
        round_message(player + 1, rounds)
        visualize_boards(board_ships, board_hits, player,
                         ships_placed[opp])
        print(HIT_MSG)
    else:
        print(MISS_MSG)
        return True


def game_loop():
    """
    Main loop of the Battleship game, managing the flow between players and 
    rounds.
    """
    # Initialize boards
    board_ships = [make_boolean_square_board(N), make_boolean_square_board(N)]
    board_hits = [make_boolean_square_board(N), make_boolean_square_board(N)]
    ships_placed = [[], []]
    player = 0
    rounds = 0
    intro(player, rounds)
    while True:
        if rounds == 0:
            place_ships(player, rounds, board_ships[player], ships_placed)
        else:
            visualize_boards(board_ships, board_hits, player,
                             ships_placed[get_opponent(player)])
            missed = False
            while not missed:
                missed = attack(player, rounds, board_ships, board_hits,
                                ships_placed)
        rounds = go_to_next_round(player, rounds)
        player = switch_player(player, rounds)


if __name__ == "__main__":
    game_loop()
