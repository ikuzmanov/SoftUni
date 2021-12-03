raw_activation_key = input()

command = input()

while command != "Generate":
    split_data = command.split(">>>")
    if split_data[0] == "Contains":
        if split_data[1] in raw_activation_key:
            print(f"{raw_activation_key} contains {split_data[1]}")
        else:
            print("Substring not found!")
    elif split_data[0] == "Flip":
        start_index = split_data[2]
        end_index = split_data[3]
        start_index = int(start_index)
        end_index = int(end_index)
        extraction = raw_activation_key[start_index:end_index]
        converted_extraction = ""
        if split_data[1] == "Upper":
            converted_extraction = extraction.upper()
        elif split_data[1] == "Lower":
            converted_extraction = extraction.lower()

        raw_activation_key = raw_activation_key.replace(extraction, converted_extraction)
        print(raw_activation_key)

    elif split_data[0] == "Slice":
        start_index, end_index = split_data[1:]
        start_index = int(start_index)
        end_index = int(end_index)
        word_to_remove = raw_activation_key[start_index:end_index]
        raw_activation_key = raw_activation_key.replace(word_to_remove, "")
        print(raw_activation_key)

    command = input()

print(f"Your activation key is: {raw_activation_key}")