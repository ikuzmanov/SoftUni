def numbers_searching(*args):
    result = []
    duplicated = []
    min_number = min(args)
    max_number = max(args)


    for num in range(min_number, max_number, 1):
        if num not in args:
            result.append(num)

    for num in args:
        if args.count(num) > 1 and num not in duplicated:
            duplicated.append(num)

    duplicated = sorted(duplicated)
    result.append(duplicated)
    return result

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
