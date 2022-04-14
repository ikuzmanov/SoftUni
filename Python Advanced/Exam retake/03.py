# def words_sorting(*args):
#     word_dict = {}
#     for word in args:
#         word_dict[word] = 0
#         for char in word:
#             word_dict[word] += ord(char)
#
#     values_sum = sum(word_dict.values())
#     if values_sum % 2 == 0:
#         sorted_values = sorted(word_dict.items(), key=lambda kvpt: kvpt[0])
#     else:
#         sorted_values = sorted(word_dict.items(), key=lambda kvpt: kvpt[1], reverse=True)
#
#
#     result = ""
#     for key,value in sorted_values:
#         result += f"{key} - {value}\n"
#     return result.strip()
#
# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#   ))
# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'eye'
#   ))
# print(
#     words_sorting(
#         'cacophony',
#         'accolade'
#   ))

a= set([1, 2, 3])
b = set([10, 11, 12])

print(a|b)