import re

text = input()
pattern = r"(@|#){1}[a-zA-z]{3,}\1{2}[a-zA-z]{3,}\1"

word_list = re.finditer(pattern, text)
word_list = ([word.group() for word in word_list])

if len(word_list) > 0:
    print(f"{len(word_list)} word pairs found!")
else:
    print("No word pairs found!")


clean_list = [word.replace("@", "").replace("#", "") for word in word_list]
mirror_words = []
for word in clean_list:
    first_part = word[:int(len(word)/2)]
    second_part = word[int(len(word)/2):]
    if second_part[::-1] == first_part:
        mirror_word = first_part + " <=> " + second_part
        mirror_words.append(mirror_word)

if len(mirror_words) > 0:
    print("The mirror words are:")
    print(", ".join(mirror_words))

else:
    print("No mirror words!")

