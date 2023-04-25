words = input().split()
words_dictionary = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in words_dictionary:
        words_dictionary[word_lower] = 0
    words_dictionary[word_lower] +=1

for key,value in words_dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
