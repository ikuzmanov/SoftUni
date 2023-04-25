def palindrome(text, index):
    if index == len(text) // 2:
        return f"{text} is a palindrome"

    left = text[index]
    right = text[len(text) - 1 - index]

    if left != right:
        return f"{text} is not a palindrome"

    return palindrome(text, index + 1)


print(palindrome('abcba', 0))
