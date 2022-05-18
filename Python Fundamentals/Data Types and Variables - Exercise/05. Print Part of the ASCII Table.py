initial_char = int(input())
last_char = int(input())

for character in range(initial_char, last_char+1):
    print(chr(character),end=" ")