
def setup():
    global board, player_signs, player_names
    board = [[' '] * 3 * 3]
    player1_name = input('Player one name: ')
    player2_name = input('Player two name: ')
    player1_sign = ''
    while player1_sign.casefold() not in ('x', 'o'):
        player1_sign = input(f'{player1_name} please choose \'X\' or \'O\': ')
    player1_sign = player1_sign.upper()
    player2_sign = 'O' if player1_sign == 'X' else 'X'
    player_signs = {1: player1_sign, 2: player2_sign}
    player_names = {1: player1_name, 2: player2_name}
    print('This is numeration of the board:')
    print('| 1 | 2 | 3 |')
    print('| 4 | 5 | 6 |')
    print('| 7 | 8 | 9 |')
    print(f'{player1_name} starts first!')
