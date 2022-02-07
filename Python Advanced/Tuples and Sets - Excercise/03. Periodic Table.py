count = int(input())
chemical_elements = set()

for _ in range(count):
    elements = input().split()
    for element in elements:
        chemical_elements.add(element)

print(*chemical_elements, sep="\n")

