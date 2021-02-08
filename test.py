board = [
    ['1', ' ', '1'],
    ['1', '1', '1'],
    ['1', ' ', '1'],
]


player_sign = '1'
rows = any([all([board[r][c] == player_sign for c in range(len(board[0]))]) for r in range(len(board))])
cols = any([all([board[r][c] == player_sign for r in range(len(board))]) for c in range(len(board[0]))])
main_diagonal = all([board[i][i] == player_sign for i in range(len(board))])
secondary_diagonal = all([board[len(board) - i - 1][i] == player_sign for i in range(len(board))])
print(rows)
print(cols)
print(main_diagonal)
print(secondary_diagonal)
