def is_inside(row, col, size, ma):
    return 0 <= row < size and 0 <= col < size and ma[row][col] != "*"


size = int(input())
bombs_count = int(input())

matrix = [[0 for element in range(size)] for element in range(size)]
for _ in range(bombs_count):
    bomb_row, bomb_col = eval(input())
    matrix[bomb_row][bomb_col] = "*"

    if is_inside(bomb_row - 1, bomb_col, size, matrix):
        matrix[bomb_row - 1][bomb_col] += 1

    if is_inside(bomb_row + 1, bomb_col, size, matrix):
        matrix[bomb_row + 1][bomb_col] += 1

    if is_inside(bomb_row, bomb_col - 1, size, matrix):
        matrix[bomb_row][bomb_col - 1] += 1

    if is_inside(bomb_row, bomb_col + 1, size, matrix):
        matrix[bomb_row][bomb_col + 1] += 1

    if is_inside(bomb_row - 1, bomb_col - 1, size, matrix):
        matrix[bomb_row - 1][bomb_col - 1] += 1

    if is_inside(bomb_row - 1, bomb_col + 1, size, matrix):
        matrix[bomb_row - 1][bomb_col + 1] += 1

    if is_inside(bomb_row + 1, bomb_col - 1, size, matrix):
        matrix[bomb_row + 1][bomb_col - 1] += 1

    if is_inside(bomb_row + 1, bomb_col + 1, size, matrix):
        matrix[bomb_row + 1][bomb_col + 1] += 1

for row in matrix:
    print(' '.join(str(el) for el in row))
