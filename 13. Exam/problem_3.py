from collections import deque


def stock_availability(inventory_list: list, mode: str, *args):
    inventory_list = deque(inventory_list)
    if mode == 'delivery':
        inventory_list.extend(args)
    if mode == 'sell':
        if args:
            if isinstance(args[0], int):
                for _ in range(args[0]):
                    inventory_list.popleft()
            elif args:
                for arg in args:
                    if arg in inventory_list:
                        inventory_list = deque([el for el in inventory_list if el != arg])
        else:
            inventory_list.popleft()
    return list(inventory_list)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))