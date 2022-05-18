data = input()
last_index = 0
result = ""

for index, char in enumerate(data):
    if char.isdigit():
        rage_text = data[last_index:index].upper()*int(char)
        last_index = index+1
        result += rage_text


unique_symbols_count = len(set(result))
print(f"Unique symbols used: {unique_symbols_count}")
print(result)