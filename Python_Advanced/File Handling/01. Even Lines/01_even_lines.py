symbols_list = ["-", ",", ", ", ".", "!", "?"]

with open("text.txt") as file:
    lines_list = file.readlines()

for index, line in enumerate(lines_list):
    if index % 2 == 0:
        for symbol in symbols_list:
            line = line.replace(symbol, "@")

        split_line = line.split()
        print(" ".join(reversed(split_line)))
