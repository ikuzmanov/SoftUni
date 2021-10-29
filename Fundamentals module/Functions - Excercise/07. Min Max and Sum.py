def sum_min_max(int_list):
    minimum_number = min(int_list)
    maximum_number = max(int_list)
    sum_of_all = sum(int_list)

    return minimum_number, maximum_number, sum_of_all

numbers = input().split(" ")
numbers_as_int = [int(i) for i in numbers]
minimum_number, maximum_number, sum_of_all = sum_min_max(numbers_as_int)
print(f"The minimum number is {minimum_number}\nThe maximum number is {maximum_number}\nThe sum number is: {sum_of_all}")
