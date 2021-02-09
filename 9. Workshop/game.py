position_mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}

board = [[' '] * 3 for _ in range(3)]
player_data = {}


def setup():
    global player_data
    player1_name = input('Player 1 name: ')
    player2_name = input('Player 2 name: ')
    player_data = {1: [player1_name], 2: [player2_name]}
    player1_sign = ''
    while player1_sign not in ('X', 'O'):
        player1_sign = input(f'{player_data[1][0]} please select X or O: ').upper()
    player2_sign = 'O' if player1_sign == 'X' else 'X'
    player_data[1].append(player1_sign)
    player_data[2].append(player2_sign)
    print('This is the numeration of the board')
    print('| 1 | 2 | 3 |')
    print('| 4 | 5 | 6 |')
    print('| 7 | 8 | 9 |')
    print(f'{player_data[1][0]} starts first!')


def get_player_choice(player_name):
    pos = input(f'{player_name} choose a free position [1-9]: ')
    return int(pos)


def position_available(pos):
    if pos in position_mapper and board[position_mapper[pos][0]][position_mapper[pos][1]] == ' ':
        return True
    return False


def execute_move(current_sign, pos):
    r, c = position_mapper[pos]
    board[r][c] = current_sign


def print_board():
    for row in board:
        print('| ' + ' | '.join(row) + ' |')


def check_win_condition(player):
    rows = any([all([board[r][c] == player for c in range(len(board[0]))]) for r in range(len(board))])
    cols = any([all([board[r][c] == player for r in range(len(board))]) for c in range(len(board[0]))])
    main_diagonal = all([board[i][i] == player for i in range(len(board))])
    secondary_diagonal = all([board[len(board) - i - 1][i] == player for i in range(len(board))])
    return any([rows, cols, main_diagonal, secondary_diagonal])


def play():
    turn_counter = 1
    while True:
        current_player = 1 if turn_counter % 2 == 1 else 2
        current_name = player_data[current_player][0]
        current_sign = player_data[current_player][1]
        pos = None
        while pos is None or not position_available(pos):
            try:
                pos = get_player_choice(current_name)
            except ValueError:
                pass
        execute_move(current_sign, pos)
        print_board()
        if check_win_condition(current_sign):
            print(f'{current_name} won!')
            break
        turn_counter += 1


if __name__ == '__main__':
    setup()
    play()
