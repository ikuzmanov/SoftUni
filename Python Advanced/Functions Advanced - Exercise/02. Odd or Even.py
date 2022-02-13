def is_odd_or_even(command, nums):
    if command == "Even":
        return sum([num for num in nums if num % 2 == 0]) * len(nums)
    elif command == "Odd":
        return sum([num for num in nums if num % 2 != 0]) * len(nums)


odd_or_even = input()
numbers_input = [int(num) for num in input().split()]

print(is_odd_or_even(odd_or_even, numbers_input))
