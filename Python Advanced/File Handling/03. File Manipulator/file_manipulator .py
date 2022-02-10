import re, os

data_input = input()

while data_input != "End":
    arguments = data_input.split("-")
    command = arguments[0]

    if command == "Create":
        file_name = arguments[1]
        with open(file_name, 'w') as file:
            pass
    if command == "Add":
        file_name, content = arguments[1:]
        with open(file_name, 'a') as file:
            file.write(content + '\n')

    if command == "Replace":
        file_name, old_string, new_string = arguments[1:]
        if os.path.exists(file_name):
            with open(file_name, 'r+') as file:
                text = file.read()
                text = re.sub(old_string, new_string, text)
                file.seek(0)
                file.write(text)
                file.truncate()
        else:
            print("An error occurred")

    if command == "Delete":
        file_name = arguments[1]
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")

    data_input = input()
