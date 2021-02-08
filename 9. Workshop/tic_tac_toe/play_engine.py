from .setup import board, player_names, player_signs
from .helpers import positions_mapper


def is_available(pos):
    if pos in positions_mapper:
        r, c = positions_mapper[pos]
        if board[r][c] == ' ':
            return True
    return False


def check_winning_condition(player_sign):
    rows = any([all([board[r][c] == player_sign for c in range(len(board[0]))]) for r in range(len(board))])
    cols = any([all([board[r][c] == player_sign for r in range(len(board))]) for c in range(len(board[0]))])
    main_diagonal = all([board[i][i] == player_sign for i in range(len(board))])
    secondary_diagonal = all([board[len(board) - i - 1][i] == player_sign for i in range(len(board))])
    if any([rows, cols, main_diagonal, secondary_diagonal]):
        return True
    return False


def print_win_message(player):
    print(f'{player_names[player]} won!')


def play_turn(player, pos):
    r, c = positions_mapper[pos]
    player_sign = player_signs[player]
    board[r][c] = player_sign
    if check_winning_condition(player_sign):
        print_win_message(player)


def play():
    turn_counter = 1
    current_player = 1 if turn_counter % 2 == 0 else 2
    current_name = player_names[current_player]
    position = None
    while not position.isdigit() and not is_available(int(position)):
        position = input(f'{current_name}, select a position (0-9): ')
    position = int(position)
    play_turn(current_player, position)
