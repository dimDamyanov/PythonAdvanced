from .setup import board, player_names, player_signs
from .helpers import positions_mapper

def is_valid(pos):
    if pos in range(1, 10):
        return True
    return False


def is_available(pos):
    r, c = positions_mapper[pos]
    if board[r][c] == ' ':
        return True
    return False


def play_turn():


def play():
    turn_counter = 1
    current_position = input(f'{player_names[turn_counter%2]}, select a position (0-9): ')
    while not current_position.isdigit() and not is_valid(int(current_position))fro:
        current_position = input(f'{player_names[turn_counter%2]}, select a position (0-9): ')
    current_position = int(current_position)
    while not is_valid(current_position):
