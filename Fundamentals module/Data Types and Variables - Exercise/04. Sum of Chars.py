number_of_lines = int(input())
result = 0

for char in range(number_of_lines):
    character = input()
    result += ord(character)

print(f"The sum equals: {result}")