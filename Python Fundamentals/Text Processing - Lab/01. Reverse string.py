word = input()

while word != "end":
    reverse_word = word[::-1]
    print(f"{word} = {reverse_word}")
    word = input()
