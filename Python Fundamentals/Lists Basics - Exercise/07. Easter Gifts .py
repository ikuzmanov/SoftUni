list_of_gifts = input().split()

command = input()

while not command == "No Money":
    command = command.split()
    if command[0] == "OutOfStock":
        for index in range(len(list_of_gifts)):
            if list_of_gifts[index] == command[1]:
                list_of_gifts[index] = None
    elif command[0] == "Required":
        if 0 <= int(command[2]) < len(list_of_gifts):
            list_of_gifts[int(command[2])] = command[1]
    elif command[0] == "JustInCase":
        list_of_gifts[-1] = command[1]
    command = input()

list_of_gifts = [element for element in list_of_gifts if element is not None]

print(" ".join(map(str,list_of_gifts)))