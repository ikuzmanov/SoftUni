matrix_size = [int(num) for num in input().split(", ")]
matrix = []
count_num = 0

for row in range(matrix_size[0]):
    row_input = [int(num) for num in input().split(", ")]
    matrix.append(row_input)
    count_num += sum(row_input)

print(count_num)
print(matrix)