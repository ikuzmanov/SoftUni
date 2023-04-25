spell_to_decipher = input()

command = input()
while command != "Abracadabra":
    split_data = command.split()

    if split_data[0] == "Abjuration":
        spell_to_decipher = spell_to_decipher.upper()
        print(spell_to_decipher)

    elif split_data[0] == "Necromancy":
        spell_to_decipher = spell_to_decipher.lower()
        print(spell_to_decipher)

    elif split_data[0] == "Illusion":
        index, letter_to_replace = int(split_data[1]), split_data[2]
        if 0 <= index < len(spell_to_decipher):
            spell_to_decipher = spell_to_decipher[:index] + letter_to_replace + spell_to_decipher[index + 1:]
        else:
            print("The spell was too weak.")

    elif split_data[0] == "Divination":
        first_substring, second_substring = split_data[1:]

        if first_substring in spell_to_decipher:
            spell_to_decipher = spell_to_decipher.replace(first_substring, second_substring, 1)
            print(spell_to_decipher)

    elif split_data[0] == "Alteration":
        substring = split_data[1]
        if substring in spell_to_decipher:
            spell_to_decipher = spell_to_decipher.replace(substring, "")
            print(spell_to_decipher)
    else:
        print("The spell did not work!")
    command = input()
