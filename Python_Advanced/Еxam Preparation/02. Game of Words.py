def move(command, row, col):
    if command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col
    elif command == "left":
        return row, col - 1
    elif command == "right":
        return row, col + 1


def is_valid_index(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


initial_string = input()
size = int(input())
matrix = []

player_row = 0
player_col = 0

for row in range(size):
    row_elements = (list(input()))
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == "P":
            player_col, player_row = col, row

commands_count = int(input())

for _ in range(commands_count):
    command = input()
    next_row, next_col = move(command, player_row, player_col)
    if is_valid_index(next_row, next_col):
        if matrix[next_row][next_col] != "-":
            initial_string += matrix[next_row][next_col]
        matrix[next_row][next_col] = "P"
        matrix[player_row][player_col] = "-"
        player_row, player_col = next_row, next_col
    else:
        if initial_string:
            initial_string = initial_string[:-1]

print(initial_string)
for row in range(size):
    print(''.join(matrix[row]))
