matrix_size = int(input())
matrix = []

primary_diagonal = []
secondary_diagonal = []

for _ in range(matrix_size):
    nums = [int(num) for num in input().split(", ")]
    matrix.append(nums)

for row in range(matrix_size):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][matrix_size -1- row])

print(f'Primary diagonal: {", ".join([str(el) for el in primary_diagonal])}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join([str(el) for el in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}')
