
def white_move(row, col):
    return row - 1, col


def black_move(row, col):
    return row + 1, col


def who_moves(turn):
    if turn % 2 == 0:
        return "White"
    else:
        return "Black"


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


matrix = []
black_row, black_col = 0, 0
white_row, white_col = 0, 0

for row in range(8):
    matrix.append([x for x in input().split()])
    for col in range(8):
        if matrix[row][col] == "b":
            black_row, black_col = row, col
        elif matrix[row][col] == "w":
            white_row, white_col = row, col

next_row, next_col = 0, 0
turns = 0
taken_white = False
taken_black = False
queen = False
while True:
    if who_moves(turns) == "White":
        matrix[white_row][white_col] = "-"
        if not is_outside(white_row - 1, white_col - 1, 8):
            if matrix[white_row - 1][white_col - 1] == "b":
                taken_white = True
                break
        if not is_outside(white_row - 1, white_col + 1, 8):
            if matrix[white_row - 1][white_col + 1] == "b":
                taken_white = True
                break
        white_row, white_col = white_move(white_row, white_col)
        matrix[white_row][white_col] = "w"
    elif who_moves(turns) == "Black":
        matrix[black_row][black_col] = "-"
        if not is_outside(black_row + 1, black_col - 1, 8):
            if matrix[black_row + 1][black_col - 1] == "w":
                taken_black = True
                break
        if not is_outside(black_row + 1, black_col + 1, 8):
            if matrix[black_row + 1][black_col + 1] == "w":
                taken_black = True
                break
        black_row, black_col = black_move(black_row, black_col)
        matrix[black_row][black_col] = "b"

    if white_row == 0 or black_row == 7:
        queen = True
        break
    turns += 1

numbered_board = []
for row in range(8, 0, -1):
    my_list = []
    for char in range(97, 105):
        my_list += [f'{chr(char)}{row}']
    numbered_board.append(my_list)

if taken_white:
    print(f'Game over! {who_moves(turns)} win, capture on {numbered_board[black_row][black_col]}.')
elif taken_black:
    print(f'Game over! {who_moves(turns)} win, capture on {numbered_board[white_row][white_col]}.')

if queen:
    print(f'Game over! {who_moves(turns)} pawn is promoted to a queen at {numbered_board[black_row][black_col] if who_moves(turns) != "White" else numbered_board[white_row][white_col]}.')