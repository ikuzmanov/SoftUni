rows, cols = [int(el) for el in input().split()]
matrix = []
pairs = 0
for _ in range(rows):
    characters = input().split()
    matrix.append(characters)

for row in range(rows-1):
    for col in range(cols-1):
        if matrix[row][col] == matrix[row + 1][col] == matrix[row][col + 1] == matrix[row + 1][col + 1]:
            pairs += 1

print(pairs)