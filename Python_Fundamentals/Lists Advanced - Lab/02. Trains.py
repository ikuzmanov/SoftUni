train_wagons_input = int(input())
train_wagons = [elem*0 for elem in range(train_wagons_input)]

command = input()
while command != "End":
    full_command = command.split(" ")
    current_command = full_command[0]
    if current_command == "add":
        people = int(full_command[1])
        train_wagons[-1] += people

    if current_command == "insert":
        index = int(full_command[1])
        people = int(full_command[2])
        train_wagons[index] += people

    if current_command == "leave":
        index = int(full_command[1])
        people = int(full_command[2])
        train_wagons[index] -= people

    command = input()

print(train_wagons)