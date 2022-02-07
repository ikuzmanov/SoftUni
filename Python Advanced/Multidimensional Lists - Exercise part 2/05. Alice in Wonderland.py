def get_next_positions(direction, row, col):
    if direction == "up":
        return row - 1, col

    if direction == "down":
        return row + 1, col

    if direction == "left":
        return row, col - 1

    if direction == "right":
        return row, col + 1


def is_outside(row, col, size):
    return row < 0 or col <0 or row >= size or col >= size


size = int(input())

matrix = []
collected_tea_bags = 0
alice_row = 0
alice_col = 0
game_over = False

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == "A":
            alice_col, alice_row = col, row


while True:
    commands = input()
    matrix[alice_row][alice_col] = "*"
    alice_row, alice_col = get_next_positions(commands, alice_row, alice_col)

    if is_outside(alice_row, alice_col, size):
        game_over = True
        break

    elif matrix[alice_row][alice_col] == "R":
        game_over = True
        matrix[alice_row][alice_col] = "*"
        break

    elif matrix[alice_row][alice_col] == ".":
        matrix[alice_row][alice_col] = "*"
        continue

    elif matrix[alice_row][alice_col].isdigit():
        collected_tea_bags += int(matrix[alice_row][alice_col])
        matrix[alice_row][alice_col] = "*"

    if collected_tea_bags >= 10:
        matrix[alice_row][alice_col] = "*"
        break


if game_over:
    print("Alice didn't make it to the tea party.")

else:
    print("She did it! She went to the party.")

for row in matrix:
    print(*row, sep=" ")
