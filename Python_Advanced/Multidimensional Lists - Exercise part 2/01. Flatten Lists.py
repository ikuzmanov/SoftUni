matrix = [[int(nums) for nums in data.split()]for data in input().split("|")]
matrix.reverse()
flatten_list = sum(matrix, [])
print(*flatten_list)
