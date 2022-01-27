rows = int(input())
result = []
for _ in range(rows):
    nums = [int(num) for num in input().split(", ")]
    result.extend(nums)

print(result)