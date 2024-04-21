from typing import List


def maxProfit(prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit

print(maxProfit([7,6,4,3,1]))
print(maxProfit([7,1,5,3,6,4]))