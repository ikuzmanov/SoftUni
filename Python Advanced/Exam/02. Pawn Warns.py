matrix = [[x for x in input().split()] for _ in range(8)]
white_x = white_y = black_x = black_y = 0

for row in range(8, 0, -1):
    for col in range(1, 9):
        if matrix[row - 1][col - 1] == 'w':
            white_x = 9 - row
            white_y = col

        if matrix[row - 1][col - 1] == 'b':
            black_x = 9 - row
            black_y = col

while white_x < 8 and black_x > 0:
    if white_x + 1 == black_x and (white_y - 1 == black_y or white_y + 1 == black_y):
        print(f'Game over! White win, capture on {chr(96 + black_y)}{black_x}.')
        break
    white_x += 1
    if white_x == 8:
        print(f'Game over! White pawn is promoted to a queen at {chr(96 + white_y)}{white_x}.')
        break

    if black_x - 1 == white_x and (black_y - 1 == white_y or black_y + 1 == white_y):
        print(f'Game over! Black win, capture on {chr(96 + white_y)}{white_x}.')
        break
    black_x -= 1
    if black_x == 1:
        print(f'Game over! Black pawn is promoted to a queen at {chr(96 + black_y)}{black_x}.')
        break


