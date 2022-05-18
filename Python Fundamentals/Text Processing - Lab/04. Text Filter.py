bad_words = input().split(", ")
full_text = input()

for word in bad_words:
    if word in full_text:
        full_text = full_text.replace(word, "*" * len(word))

print(full_text)
