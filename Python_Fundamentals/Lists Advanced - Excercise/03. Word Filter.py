word_input = input().split()
print('\n'.join(word for word in word_input if len(word)%2 == 0))
