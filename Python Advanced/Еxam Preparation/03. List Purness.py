def best_list_pureness(*param):
    result_count = 0
    max_number = 0
    max_index = 0
    num_list, rotation_count = param[0], param[1]
    for count in range(0, rotation_count + 1):
        for index, num in enumerate(num_list):
            result_count += index * num

        if result_count > max_number:
            max_number = result_count
            max_index = count

        result_count = 0
        popped_num = num_list.pop()
        num_list.insert(0, popped_num)

    return f"Best pureness {max_number} after {max_index} rotations"


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
