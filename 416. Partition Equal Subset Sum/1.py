from typing import List

def canPartition(nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        memo = {}
        return (dfs(nums, len(nums) - 1, int(total / 2), memo))
        
def dfs(nums, index, target, memo):
    if (index, target) in memo:
        return memo[(index, target)]
    if target == 0:
        return True
    if target < 0 or index == 0:
        return False
    
    
    ra = dfs(nums, index - 1, target - nums[index], memo)
    rb = dfs(nums, index - 1, target, memo)
    if ra or rb:
        return True
    if not ra and not rb:
        memo[(index, target)] = False
    
    
    
    return False

canPartition([1,5,11,5])
