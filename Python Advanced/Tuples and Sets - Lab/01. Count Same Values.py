nums_input = tuple(float(num) for num in input().split())
new_list = []
[new_list.append(num) for num in nums_input if num not in new_list]

for num in new_list:
    print(f"{num} - {nums_input.count(num)} times")