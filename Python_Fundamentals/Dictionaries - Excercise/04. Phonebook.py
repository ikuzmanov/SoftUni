name_and_number = input()
phonebook = {}
while not name_and_number.isdigit():
    name, number = name_and_number.split("-")
    phonebook[name] = number

    name_and_number = input()
for _ in range(int(name_and_number)):
    searched_name = input()
    if searched_name in phonebook:
        print(f'{searched_name} -> {phonebook[searched_name]}')
    else:
        print(f'Contact {searched_name} does not exist.')