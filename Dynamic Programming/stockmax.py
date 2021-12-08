# https://www.hackerrank.com/challenges/stockmax/


def stockmax(prices):
    bought_shares = 0
    profit = 0
    max_price_for_stock = max(prices)

    while prices:
        p = prices.pop(0)
        if p < max_price_for_stock:
            # Buy shares.
            bought_shares += 1
            profit -= p
        elif p == max_price_for_stock:
            # Sell shares.
            profit += bought_shares * p
            bought_shares = 0
            if prices:
                max_price_for_stock = max(prices)

    return profit
