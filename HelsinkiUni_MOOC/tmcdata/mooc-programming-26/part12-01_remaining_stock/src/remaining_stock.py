# Write your solution here:

def sort_by_remaining_stock(items: list) -> list:
    stock = sorted(items, key=lambda x: x[2])

    return stock



if __name__ == '__main__':
    products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)]

    print(sort_by_remaining_stock(products))


