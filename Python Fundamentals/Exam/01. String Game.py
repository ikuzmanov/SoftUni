string = input()

command = input()

while command != "Done":
    split_data = command.split()
    if split_data[0] == "Change":
        char, replacement = split_data[1:]
        string = string.replace(char, replacement)
        print(string)
    elif split_data[0] == "Includes":
        substring = split_data[1]
        if substring in string:
            print(True)
        else:
            print(False)
    elif split_data[0] == "End":
        substring = split_data[1]
        print(string.endswith(substring))
    elif split_data[0] == "Uppercase":
        string = string.upper()
        print(string)
    elif split_data[0] == "FindIndex":
        char = split_data[1]
        index_of_char = string.index(char)
        print(index_of_char)
    elif split_data[0] == "Cut":
        start_index, count = int(split_data[1]), int(split_data[2])
        cut_string = string[start_index:start_index+count]
        print(cut_string)
    command = input()