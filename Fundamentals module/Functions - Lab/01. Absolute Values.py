args = input().split(" ")
final_list = []
float_nums = [float(i) for i in args]

for num in float_nums:
    final_list.append(abs(num))

print(final_list)