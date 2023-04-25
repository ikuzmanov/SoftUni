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


size = 6

matrix = []

rover_row = 0
rover_col = 0

deposits_collection = {
    "Water": 0,
    "Metal": 0,
    "Concrete": 0,
}
is_broken = False

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(size):
        if row_elements[col] == "E":
            rover_row, rover_col = row, col

commands_list = input().split(", ")
for direction in commands_list:


    next_row, next_col = get_next_positions(direction, rover_row, rover_col)

    if matrix[next_row][next_col] == "R":
        is_broken = True
        print(f"Rover got broken at ({next_row}, {next_col})")
        break

    if matrix[next_row][next_col] == "W":
        deposits_collection["Water"] += 1
        print(f"Water deposit found at ({next_row}, {next_col})")

    if matrix[next_row][next_col] == "M":
        deposits_collection["Metal"] += 1
        print(f"Metal deposit found at ({next_row}, {next_col})")

    if matrix[next_row][next_col] == "C":
        deposits_collection["Concrete"] += 1
        print(f"Concrete deposit found at ({next_row}, {next_col})")

    rover_row, rover_col = next_row, next_col

is_area_suitable = [True if num >= 1 else False for num in deposits_collection.values()]
if all(is_area_suitable):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
