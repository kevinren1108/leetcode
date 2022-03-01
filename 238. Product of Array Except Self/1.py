from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * n
    prefix = [0] * n
    postfix = [0] * n
    
    prefix[0] = nums[0]
    for i in range(1,n):
        prefix[i] = prefix[i-1] * nums[i]
    # [1,2,6,24]
    postfix[-1] = nums[-1]
    for i in range(2,n+1):
        postfix[-i] = postfix[-i+1] * nums[-i]
    # [24,24,12,4]    
    
    res[0] = postfix[1]
    res[-1] = prefix[-2]
    for i in range(1,n-1):
        res[i] = prefix[i-1] * postfix[i+1]
    
    return res


#follow up question can you find O(1) space solution?
#yes you can, dont compute prefix and postfix until run
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * n
    prefix = 1
    postfix = 1
    
    
    
    res[0] = 1
    for i in range(1,n):
        res[i] = prefix
        prefix = nums[i] * prefix
    
    # [1, 1, 2, 6]
    
    for i in range(n-2,-1,-1):
        print(i)
    
    return res
            