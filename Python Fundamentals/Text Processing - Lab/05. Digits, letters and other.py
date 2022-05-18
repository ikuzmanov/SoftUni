text_input = input()

nums = ""
alphas = ""
other = ""

for char in text_input:
    if char.isdigit():
        nums += char
    elif char.isalpha():
        alphas += char
    else:
        other += char

print(nums)
print(alphas)
print(other)
