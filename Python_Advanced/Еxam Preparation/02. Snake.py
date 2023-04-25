def get_next_position(direction, row, col):
    if direction == "up":
        return row - 1, col

    if direction == "down":
        return row + 1, col

    if direction == "left":
        return row, col - 1

    if direction == "right":
        return row, col + 1


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


size = int(input())
burrow_1_row = 0
burrow_1_col = 0

burrow_2_row = 0
burrow_2_col = 0
snake_row = 0
snake_col = 0

food_count = 0
game_over = False

matrix = []
for row in range(size):
    matrix.append(list(input()))
    if 'S' in matrix[row]:
        snake_row = row
        snake_col = matrix[row].index('S')

    if 'B' in matrix[row] and matrix[burrow_1_row][burrow_1_col] != "B":
        burrow_1_row = row
        burrow_1_col = matrix[row].index('B')

    if 'B' in matrix[row]:
        burrow_2_row = row
        burrow_2_col = matrix[row].index('B')

while True:
    if food_count >= 10:
        break

    command = input()
    next_row, next_col = get_next_position(command, snake_row, snake_col)

    if is_outside(next_row, next_col, size):
        matrix[snake_row][snake_col] = "."
        game_over = True
        break

    if matrix[next_row][next_col] == "*":
        food_count += 1

    if matrix[next_row][next_col] == "B":

        if next_row == burrow_1_row and next_col == burrow_1_col:
            next_row, next_col = burrow_2_row, burrow_2_col
            matrix[burrow_1_row][burrow_1_col] = "."

        elif next_row == burrow_2_row and next_col == burrow_2_col:
            next_row, next_col = burrow_1_row, burrow_1_col
            matrix[burrow_2_row][burrow_2_col] = "."

    matrix[next_row][next_col] = "S"
    matrix[snake_row][snake_col] = "."
    snake_row, snake_col = next_row, next_col

if game_over:
    print("Game over!")

if food_count >= 10:
    print("You won! You fed the snake.")

print(f"Food eaten: {food_count}")

for row in matrix:
    print(''.join(row))
