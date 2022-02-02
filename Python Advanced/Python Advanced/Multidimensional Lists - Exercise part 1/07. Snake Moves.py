rows, cols = [int(x) for x in input().split()]
word = input()

index = 0

matrix = []

for row in range(rows):
    row_elements = []
    for col in range(cols):
        row_elements.append(word[index % len(word)])
        index += 1
    if row % 2 == 0:
        print(*row_elements, sep="")
    else:
        print(*reversed(row_elements), sep="")
