# WA on testcase 179


from math import inf
from typing import List

def maxProfit(k: int, prices: List[int]) -> int:
    n = len(prices)
    if not n: return 0
    
    sold = [[0 for i in range(k)] for j in range(len(prices))]
    hold = [[0 for i in range(k)] for j in range(len(prices))]
    
    sold[0][0] = 0
    hold[0][0] = -prices[0]
    
    for i in range(1, len(prices)):
        for j in range(0, k):
            if j - 1 >= 0:
                sold[i][j] = max(sold[i-1][j], hold[i-1][j-1] + prices[i])
                hold[i][j] = max(hold[i-1][j], sold[i-1][j] - prices[i])
            else:
                sold[i][j] = max(sold[i-1][j], hold[i-1][j] + prices[i])
                hold[i][j] = max(hold[i-1][j], sold[i-1][j] - prices[i])
        
    print(sold)
    
    maxProfit = -float(inf)
    for j in range(0,k):
        maxProfit = max(maxProfit, sold[len(prices)-1][j])
        
    return maxProfit

maxProfit(2,[3,3,5,0,0,3,1,4])