def maxProfit(prices) -> int:
    mininum = prices[0]
    maximum = 0
    for i in prices:
        mininum = min(mininum, i)
        maximum = max(maximum, i - mininum)
    return maximum

prices = [7,1,5,3,6,4]
print(maxProfit(prices))