text = input()

filtered_letters = ""
last_letter = ""

for current_letter in text:
    if current_letter != last_letter:
        filtered_letters += current_letter
        last_letter = current_letter

print(filtered_letters)