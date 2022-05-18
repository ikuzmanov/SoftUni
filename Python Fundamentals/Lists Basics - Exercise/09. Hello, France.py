price_type = input().split('|')
budget = float(input())
bought_items = []
sales_budget = 0
profit = 0
is_france = False

for i in price_type:
    split_i = i.split('->')
    items_type = split_i[0]
    item_price = float(split_i[1])

    if budget - item_price >= 0 and item_price <= 50.00 and items_type == 'Clothes':
        bought_items.append(f'{(item_price * 1.4):.2f}')
        budget -= float(item_price)
        sales_budget += 1.4 * item_price
        profit += 0.4 * item_price
    elif budget - item_price >= 0 and item_price <= 35.00 and items_type == 'Shoes':
        bought_items.append(f'{(item_price * 1.4):.2f}')
        budget -= float(item_price)
        sales_budget += 1.4 * item_price
        profit += 0.4 * item_price
    elif budget - item_price >= 0 and item_price <= 20.50 and items_type == 'Accessories':
        bought_items.append(f'{(item_price * 1.4):.2f}')
        budget -= float(item_price)
        sales_budget += 1.4 * item_price
        profit += 0.4 * item_price
    if budget + sales_budget >= 150.00:
        is_france = True

for index in bought_items:
    item = float(index)
    print(f'{item:.2f}', end=' ')
print()
print(f'Profit: {profit:.2f}')
if is_france:
    print('Hello, France!')
else:
    print('Not enough money.')