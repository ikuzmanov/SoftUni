def is_inside(rows, columns, size):
    return 0 <= rows < size and 0 <= columns < size


rows_from_input = int(input())

matrix = []

for _ in range(rows_from_input):
    nums = [int(num) for num in input().split()]
    matrix.append(nums)

data = input()

while data != "END":
    command = data.split()
    row, col, value = int(command[1]), int(command[2]), int(command[3])
    if is_inside(row, col, rows_from_input):
        if command[0] == "Add":
            matrix[row][col] += value

        elif command[0] == "Subtract":
            matrix[row][col] -= value

    else:
        print("Invalid coordinates")

    data = input()

for row in matrix:
    print(*row)