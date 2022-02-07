input_data = tuple(input())

sorted_set = sorted(set(input_data))

for char in sorted_set:
    print(f"{char}: {input_data.count(char)} time/s")
