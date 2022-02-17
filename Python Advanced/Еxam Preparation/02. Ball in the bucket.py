def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size

size = 6

matrix = [input().split() for _ in range(size)]

points_collected = 0


for _ in range(3):
    coordinates = input().strip("()").split(", ")
    current_row, current_col = int(coordinates[0]), int(coordinates[1])

    if is_outside(current_row, current_col, size):
        continue

    if matrix[current_row][current_col] == "B":
        for row in range(len(matrix)):
            current_position = matrix[row][current_col]
            if current_position != "B":
                points_collected += int(current_position)
                matrix[row][current_col] = 0

if points_collected < 100:
    print(f"Sorry! You need {100-points_collected} points more to win a prize.")

elif points_collected >= 300:
    print(f"Good job! You scored {points_collected} points, and you've won Lego Construction Set.")

elif 200 <= points_collected < 300:
    print(f"Good job! You scored {points_collected} points, and you've won Teddy Bear.")

else:
    print(f"Good job! You scored {points_collected} points, and you've won Football.")
