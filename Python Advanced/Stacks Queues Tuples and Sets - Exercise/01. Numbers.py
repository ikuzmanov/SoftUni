first_set = set([int(num) for num in input().split()])
second_set = set([int(num) for num in input().split()])

commands_count = int(input())

for _ in range(commands_count):
    input_data = input().split()
    first_command, second_command = input_data[0], input_data[1]

    if first_command == "Add":
        nums = tuple([int(num) for num in (input_data[2::])])
        if second_command == "First":
            first_set.update(nums)
        elif second_command == "Second":
            second_set.update(nums)

    elif first_command == "Remove":
        nums = tuple([int(num) for num in (input_data[2::])])
        if second_command == "First":
            first_set.difference_update(nums)
        elif second_command == "Second":
            second_set.difference_update(nums)

    elif first_command == "Check" and second_command == "Subset":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
