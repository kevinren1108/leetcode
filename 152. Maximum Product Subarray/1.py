from typing import List


def maxProduct(nums: List[int]) -> int:
    
    res = max(nums)
    minProd, maxProd = 1, 1
    
    for n in nums:
        tmp = maxProd * n
        maxProd = max(minProd * n, maxProd * n, n)
        minProd = min(tmp, minProd * n, n)
        res = max(res, maxProd, minProd)
        
    return res

maxProduct([2,3,-2,4])