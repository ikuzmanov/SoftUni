def sorting_numbers(num_list):
    return sorted(num_list)

numbers_input = input().split(" ")
numbers_as_digits = [int(i) for i in numbers_input]

sorted_numbers = sorting_numbers(numbers_as_digits)
print(sorted_numbers)