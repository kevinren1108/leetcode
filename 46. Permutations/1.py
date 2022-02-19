from typing import List

def permute( nums: List[int]) -> List[List[int]]:
    ans = []
    path = []
    
    def backTracking(nums):
        if not nums:
            ans.append(path.copy())
            # return
        for i in range(0, len(nums)):
            path.append(nums[i])
            
            backTracking(nums[:i]+nums[i+1:])
            path.pop()

    backTracking(nums)
    return ans

permute([1,2,3])