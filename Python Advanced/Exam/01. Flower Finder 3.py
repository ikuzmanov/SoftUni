from collections import deque

vowels = deque(input().split())
consonants = input().split()

rose = set("rose")
tulip = set("tulip")
lotus = set("lotus")
daffodil = set("daffodil")
needed_letters = rose.union(tulip).union(lotus).union(daffodil)
word_found = False
collected_letters = set()

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    if current_vowel in needed_letters:
        collected_letters.add(current_vowel)
    if current_consonant in needed_letters:
        collected_letters.add(current_consonant)
    if rose.issubset(collected_letters):
        print("Word found: rose")
        word_found = True
        break
    if tulip.issubset(collected_letters):
        print("Word found: tulip")
        word_found = True
        break
    if lotus.issubset(collected_letters):
        print("Word found: lotus")
        word_found = True
        break
    if daffodil.issubset(collected_letters):
        print("Word found: daffodil")
        word_found = True
        break

if not word_found:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")