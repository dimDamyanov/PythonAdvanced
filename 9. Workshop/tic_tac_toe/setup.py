board = None
player_signs = None
player_names = None


def setup():
    global player1_name, player2_name
    global board
    board = [[' '] * 3 * 3]
    player1_name = input('Enter player 1 name: ')
    player2_name = input('Enter player 2 name: ')
    player1_sign = None
    while player1_sign.casefold() not in ('x', 'o'):
        player1_sign = input('Player 1, please select sign X or O: ')
    player1_sign = player1_sign.upper()
    player2_sign = 'O' if player1_sign == 'X' else 'X'
    global player_signs, player_names
    player_signs = {1: player1_sign, 0: player2_sign}
    player_names = {1: player1_name, 0: player2_name}
    print('This is numeration of the board')
    print('|1|2|3|')
    print('|4|5|6|')
    print('|7|8|9|')
    print('Player one starts first')