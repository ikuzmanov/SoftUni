count_lines = int(input())

final_set1 = set()
final_set2 = set()
max_intersection = set()

for _ in range(count_lines):
    sets_from_input = tuple(input().split("-"))
    set1, set2 = sets_from_input
    set1, set2 = set1.split(","), set2.split(",")

    for num in range(int(set1[0]), int(set1[-1])+1):
        final_set1.add(num)

    for num in range(int(set2[0]), int(set2[-1])+1):
        final_set2.add(num)

    intersection = final_set1.intersection(final_set2)
    if len(intersection) > len(max_intersection):
        max_intersection = intersection

    final_set1.clear()
    final_set2.clear()

print(f"Longest intersection is {[num for num in max_intersection]} with length {len(max_intersection)}")

