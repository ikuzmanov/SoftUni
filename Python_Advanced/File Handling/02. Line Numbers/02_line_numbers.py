import re
with open('text.txt') as input_file, open('output.txt', 'w') as output_file:
    for index, line in enumerate(input_file):
        stripped_line = line.strip()
        letters_count = len(re.findall('[A-Za-z]', stripped_line))
        punctuation_count = len(re.findall('[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', stripped_line))
        output_file.write(f"Line {index + 1}: {stripped_line} ({letters_count})({punctuation_count})\n")
