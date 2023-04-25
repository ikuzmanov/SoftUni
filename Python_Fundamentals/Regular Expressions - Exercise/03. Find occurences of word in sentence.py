import re

sentence = input().lower()
needed_word = input().lower()

pattern = fr"\b{needed_word}\b"
match = re.findall(pattern, sentence)

print(len(match))