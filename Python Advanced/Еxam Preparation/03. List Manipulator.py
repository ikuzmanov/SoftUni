def list_manipulator(numbers_list, command, location, *args):
    if command == "add":

        if location == "beginning":
            numbers_list = list(args) + numbers_list
            return numbers_list

        elif location == "end":
            numbers_list += args

    elif command == "remove":

        if location == "beginning":
            if not args:
                numbers_list = numbers_list[1::]
            else:
                numbers_to_remove, = args
                del numbers_list[:-numbers_to_remove + 1]

        elif location == "end":
            if not args:
                numbers_list.pop()
            else:
                numbers_to_remove, = args
                del numbers_list[-numbers_to_remove:]

    return numbers_list


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
