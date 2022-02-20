from collections import deque

vowels = deque(input().split(' '))
consonants = deque(input().split(' '))

flowers = ['rose', 'tulip', 'lotus', 'daffodil']
letters_found = []
is_found = False
flower_found = ''
while vowels and consonants or is_found:
    vow = vowels.popleft()
    cons = consonants.pop()
    for flower in flowers:
        if vow in flower:
            letters_found.append(vow)
        if cons in flower:
            letters_found.append(cons)
        letter_match = 0
        for el in flower:
            word_len = len(flower)
            if el in letters_found:
                letter_match += 1
            if word_len == letter_match:
                is_found = True
                flower_found= flower
                break
    if is_found:
        break

if is_found:
    print(f'Word found: {flower_found}')
    if vowels:
        print(f'Vowels left: {" ".join(vowels)}')
    if consonants:
        print(f'Consonants left: {" ".join(consonants)}')
else:
    print(f'Cannot find any word!')
    if vowels:
        print(f'Vowels left: {" ".join(vowels)}')
    if consonants:
        print(f'Consonants left: {" ".join(consonants)}')