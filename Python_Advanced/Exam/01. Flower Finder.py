from collections import deque


vowels = deque([x for x in input().split()])
consonants = [x for x in input().split()]

matches_list = ["rose", "tulip", "lotus", "daffodil"]
temp_list = []
found_flower = ""
found = False

while True:
    if not vowels or not consonants:
        break
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for idx, flower in enumerate(matches_list):
        for char in flower:
            if char == current_vowel:
                temp_list.append(char)
            elif char == current_consonant:
                temp_list.append(char)

    for flower1 in matches_list:
        for character in flower1:
            if character in temp_list:
                found_flower += character
            else:
                break
        if found_flower in matches_list:
            found = True
            break
        if found:
            break
        else:
            found_flower = ""
    if found:
        break


if not found:
    print('Cannot find any word!')
else:
    print(f'Word found: {found_flower}')

if vowels:
    print(f'Vowels left: {" ".join(str(x) for x in vowels)}')

if consonants:
    print(f'Consonants left: {" ".join(str(x) for x in consonants)}')