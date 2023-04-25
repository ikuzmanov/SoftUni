string_seq = input().split()

for word in string_seq:
    word_len = len(word)
    print(word*word_len, end="")