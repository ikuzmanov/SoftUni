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
        lower_or_upper, start_index, end_index = split_data[1:]
        start_index, end_index = int(start_index), int(end_index)

        if lower_or_upper == "Upper":
            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].upper() + raw_activation_key[end_index:]

        elif lower_or_upper == "Lower":
            converted_extraction = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].lower() + raw_activation_key[end_index:]

        print(raw_activation_key)

    elif split_data[0] == "Slice":
        start_index, end_index = split_data[1:]
        start_index, end_index = int(start_index), int(end_index)
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)

    command = input()

print(f"Your activation key is: {raw_activation_key}")