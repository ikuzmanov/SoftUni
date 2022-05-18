text = input()
vowels = ["a", "o", "u", "e", "i"]

no_vowels = [char for char in text if char not in vowels]

print("".join(no_vowels))