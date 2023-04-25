data = input()
cipher = ""
for char in data:
    new_char_ascii = ord(char)+3
    new_char_converted = chr(new_char_ascii)
    cipher += new_char_converted

print(cipher)