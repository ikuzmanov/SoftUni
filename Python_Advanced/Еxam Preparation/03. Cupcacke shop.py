def stock_availability(inventory, command, *args):
    if command == "delivery":
        inventory.extend(args)
    elif command == "sell":
        if args:
            if isinstance(args[0], int):
                for _ in range(args[0]):
                    inventory = inventory[args[0]:]
            else:
                for arg in args:
                    if arg in inventory:
                        inventory = list(filter(lambda x: x != arg, inventory))
        else:
            inventory.pop(0)
    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
