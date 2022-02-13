def is_negative(num):
    if num < 0:
        return True
    return False


positive_nums = 0
negative_nums = 0

nums_input = [int(num) for num in input().split()]

for num in nums_input:
    if is_negative(num):
        negative_nums += num
    else:
        positive_nums += num

print(negative_nums)
print(positive_nums)

if abs(negative_nums) > abs(positive_nums):
    print("The negatives are stronger than the positives")

else:
    print("The positives are stronger than the negatives")
