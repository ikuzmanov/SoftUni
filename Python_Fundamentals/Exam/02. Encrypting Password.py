import re

pattern = r"^(.+)>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1$"

count = int(input())

for _ in range(count):
    password_input = input()
    if re.search(pattern, password_input) is None:
        print("Try another password!")
    else:
        result = re.finditer(pattern, password_input)
        for match in result:
            password = match.group(2) + match.group(3) + match.group(4) + match.group(5)
            print(f"Password: {password}")