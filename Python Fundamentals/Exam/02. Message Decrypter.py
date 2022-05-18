import re

pattern = r"^(\$|%)([A-Z][a-z]{2,})(\1):\s\[([0-9]+)]\|\[([0-9]+)]\|\[([0-9]+)]\|$"
count = int(input())

for _ in range(count):
    password_input = input()
    if re.search(pattern, password_input) is None:
        print("Valid message not found!")
    else:
        result = re.finditer(pattern, password_input)
        for match in result:
            tag = match.group(2)
            message = chr(int(match.group(4))) + chr(int(match.group(5))) + chr(int(match.group(6)))
            print(f"{tag}: {message}")