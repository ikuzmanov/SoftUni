data = input().split()
searched_products = input().split()

products = {}

for index in range(0,len(data), 2):
    key = data[index]
    value = int(data[index+1])
    products[key] = value


for searched_word in searched_products:
    if searched_word in products:
        print(f"We have {products[searched_word]} of {searched_word} left")
    else:
        print(f"Sorry, we don't have {searched_word}")