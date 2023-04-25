count = int(input())

piano_collection = {}

for _ in range(count):
    piece, composer, key = input().split("|")
    piano_collection[piece] = {"composer": composer, "key": key}

command = input()

while command != "Stop":
    split_data = command.split("|")

    if split_data[0] == "Add":
        piece, composer, key = split_data[1:]
        if piece not in piano_collection:
            piano_collection[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif split_data[0] == "Remove":
        piece = split_data[1]
        if piece in piano_collection:
            del piano_collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif split_data[0] == "ChangeKey":
        piece, new_key = split_data[1:]
        if piece in piano_collection:
            piano_collection[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

sorted_piano = sorted(piano_collection.items(), key=lambda kvpt: (kvpt[0], kvpt[1]["composer"]))

for piece, data in sorted_piano:
    print(f"{piece} -> Composer: {data['composer']}, Key: {data['key']}")
