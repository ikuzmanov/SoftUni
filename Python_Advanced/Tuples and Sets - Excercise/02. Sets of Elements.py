num_input = [int(num) for num in input().split()]

set_1 = set()
set_2 = set()

for _ in range(num_input[0]):
    nums_for_set_1 = int(input())
    set_1.add(nums_for_set_1)

for _ in range(num_input[1]):
    nums_for_set_2 = int(input())
    set_2.add(nums_for_set_2)

intersection = set_1.intersection(set_2)
print(*intersection, sep="\n")