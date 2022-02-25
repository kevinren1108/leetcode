def maxProfit(self, prices: List[int]) -> int:
    maxProfit,minPrice = 0,float(inf)
    for price in prices:
        minPrice = min(price,minPrice)
        profit = price - minPrice
        maxProfit = max(maxProfit,profit)
    return maxProfit