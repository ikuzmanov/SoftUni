def get_next_positions(direction, row, col):
    if direction == "up":
        if row > 0:
            return row - 1, col
        return size - 1, col

    if direction == "down":
        if row < size - 1:
            return row + 1, col
        return 0, col

    if direction == "left":
        if col > 0:
            return row, col - 1
        return row, size - 1

    if direction == "right":
        if col < size - 1:
            return row, col + 1
        return row, 0


size = int(input())

matrix = []

player_row = 0
player_col = 0

coins_collected = 0

game_over = False

coordinates = []

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == "P":
            player_col, player_row = col, row
coordinates.append([player_row, player_col])
while coins_collected < 100:
    commands = input()
    player_row, player_col = get_next_positions(commands, player_row, player_col)

    if matrix[player_row][player_col] == "X":
        game_over = True
        coins_collected = int(coins_collected / 2)
        coordinates.append([player_row, player_col])
        break

    elif matrix[player_row][player_col] != "P":
        coins_collected += int(matrix[player_row][player_col])

    coordinates.append([player_row, player_col])
    matrix[player_row][player_col] = 0

if game_over:
    print(f"Game over! You've collected {coins_collected} coins.")
    print("Your path:")
    print(*coordinates, sep="\n")
else:
    print(f"You won! You've collected {coins_collected} coins.")
    print("Your path:")
    print(*coordinates, sep="\n")
