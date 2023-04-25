import re

pattern = r"((www)\.([a-zA-Z0-9]+(\-[a-zA-Z0-9]+)*(\.[a-z]+)+))"
some_sentence = input()
valid_urls = []
while some_sentence:
    matches = re.finditer(pattern, some_sentence)
    for match in matches:
        print(match.group(1))
    some_sentence = input()

