import re

string = input()
pattern = r"\b_([a-zA-Z0-9]+)\b"
matches = re.findall(pattern, string)
print(",".join(matches))