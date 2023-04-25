rows, cols = 8, 8

board = []
white = ''
black = ''
winner = False

for row in range(rows):
    line = [el for el in input().split(' ')]
    board.append(line)
    if 'w' in line:
        white = [row, line.index('w')]
    if 'b' in line:
        black = [row, line.index('b')]

coor_board = []

for row in range(8):
    coor_board.append([f'' for el in range(8)])
    for col in range(8):
        coor_board[row][col] = f'{chr(97 + col)}{8 - row}'

while not winner:
    if white[0] - black[0] == 1:
        if white[1] - black[1] == 1 or black[1] - white[1] == 1:
            winner = True
            print(f'Game over! White win, capture on {coor_board[black[0]][black[1]]}.')
            break
    white[0] -= 1
    if white[0] == 0:
        winner = True
        print(f'Game over! White pawn is promoted to a queen at {coor_board[white[0]][white[1]]}.')
        break
    if black[0] - white[0] == -1:
        if black[1] - white[1] == 1 or white[1] - black[1] == 1:
            winner = True
            print(f'Game over! Black win, capture on {coor_board[white[0]][white[1]]}.')
            break
    black[0] += 1
    if black[0] == 7:
        winner = True
        print(f'Game over! Black pawn is promoted to a queen at {coor_board[black[0]][black[1]]}.')
        break