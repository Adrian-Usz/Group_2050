def recursive_total_price(products) -> float:
    if products == []:
        return 0.0
    return products[-1].price + recursive_total_price(products[:-1])

def fewest_coins(coins, amount, memo = None) -> int:
    if memo is None:
        memo = {}
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    if amount in memo:
        return memo[amount]
    best = float('inf')
    for coin in coins:
        best = min(best, 1 + fewest_coins(amount - coin, coins, memo))
    memo[amount] = best
    return best

def bubble_sort(products) -> None:
    for j in range(len(products) - 1):
            for i in range(len(products) - 1 - j):
                if products[i].get_id() > products[i+1].get_id():
                    products[i], products[i+1] = products[i+1], products[i]

def selection_sort(products) -> None:
    n = len(products)
    for i in range(n-1):
        index_of_max = 0
        for index in range(n-i):
            if products[index].get_id() > products[index_of_max].get_id():
                index_of_max = index
        products[n - i - 1], products[index_of_max] = products[index_of_max], products[n - i -1]

def insertion_sort(products) -> None:
    n = len(products)
    for i in range(n):
        j = n - i - 1
        while j < n - 1 and (products[j].get_id() > products[j+1].get_id()):
            products[j], products[j+1] = products[j+1], products[j]
            j += 1

def binary_search(products, product_id) -> int:
    if len(products) == 0:
        return -1
    median = len(products) // 2
    if product_id == products[median].get_id():
        return median
    elif product_id < products[median].get_id():
        return binary_search(products[:median], product_id)
    elif product_id > products[median].get_id():
        return binary_search(products[median + 1:], product_id)