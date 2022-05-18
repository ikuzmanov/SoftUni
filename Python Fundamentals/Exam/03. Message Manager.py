manager = {}

message_capacity = int(input())

command = input()

while command != 'Statistics':
    split_data = command.split("=")
    if split_data[0] == "Add":
        username, sent, received = split_data[1], int(split_data[2]), int(split_data[3])
        if not username in manager:
            manager[username] = {"sent": sent, "received": received}

    elif split_data[0] == "Message":
        sender, receiver = split_data[1:]
        if sender and receiver in manager:
            manager[sender]["sent"] += 1
            manager[receiver]["received"] += 1

            if manager[sender]["sent"] + manager[sender]["received"] >= 10:
                del manager[sender]
                print(f"{sender} reached the capacity!")
            if manager[receiver]["sent"] + manager[receiver]["received"] >= 10:
                del manager[receiver]
                print(f"{receiver} reached the capacity!")

    elif split_data[0] == "Empty":
        if split_data[1] == "All":
            manager = manager.clear()
        else:
            username = split_data[1]
            if username in manager:
                del manager[username]

    command = input()

print(f"Users count: {len(manager)}")
sorted_manager = sorted(manager.items(), key = lambda kvpt: (-(kvpt[1]["sent"] + kvpt[1]["received"]), kvpt[0]))

for username, data in sorted_manager:
    total_messages = data["sent"] + data["received"]
    print(f"{username} - {total_messages}")