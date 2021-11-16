text_input = input().split()

chars = {}

for word in text_input:
    for char in word:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1

for character, occurences in chars.items():
    print(f"{character} -> {occurences}")
