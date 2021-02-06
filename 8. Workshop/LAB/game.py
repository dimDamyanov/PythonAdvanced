DEFAULT_ROWS_COUNT = 6
DEFAULT_COLUMNS_COUNT = 7
WIN_LEN = 4

def print_board(board):
    [print(row) for row in board]


def print_winnner_message(player):
    print(f'The winner is player {player}')


def get_player_choice(player):
    print(f'Player {player}, please choose a column')
    return int(input()) - 1


def get_lowest_row_index(board, column):
    rows_count = len(board)
    for row_index in range(rows_count - 1, -1, -1):
        if board[row_index][column] == 0:
            return row_index
    return None


def apply_player_choice(board, column_index, player):
    row_index = get_lowest_row_index(board, column_index)
    board[row_index][column_index] = player
    pass


def play(board, player=1):
    while True:
        player_choice = get_player_choice(player)
        apply_player_choice(board, player_choice, player)
        print_board(board)
        if check_win_condition(board, player):
            print_winnner_message(player)
            return
        player = 2 if player == 1 else 1


def in_range(value, max_value):
    return 0 <= value < max_value


def check_win_condition_from_position(board, row_index, column_index, player, win_condition=WIN_LEN):
    rows_count = len(board)
    columns_count = len(board[0])
    end_column_index = column_index + win_condition
    end_row_index = row_index + win_condition
    horizontal_values = [in_range(c, columns_count) and board[row_index][c] == player for c in range(column_index, end_column_index)]
    vertical_values = [in_range(r, rows_count) and board[r][column_index] == player for r in range(row_index, end_row_index)]
    return all(horizontal_values) or all(vertical_values)


def check_win_condition(board, player):
    rows_count = len(board)
    for row_index in range(rows_count):
        columns_count = len(board[row_index])
        for column_index in range(columns_count):
            if check_win_condition_from_position(board, row_index, column_index, player):
                return True
            return False


def create_board(rows_count=DEFAULT_ROWS_COUNT, columns_count=DEFAULT_COLUMNS_COUNT):
    return [[0] * columns_count for _ in range(rows_count)]


def main():
    board = create_board()
    play(board)


if __name__ == '__main__':
    main()
