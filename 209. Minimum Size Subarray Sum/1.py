from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    l = 0

    #sliding window, if sum < target R++, else L ++
    sum = 0
    minLen = 999999
    
    for r in range(0,len(nums)):
        sum += nums[r]
        
        while sum >= target:
            minLen = min(minLen,r-l+1)
            sum -= nums[l]
            l += 1
        
            
    return minLen    


minSubArrayLen(7,[2,3,1,2,4,3])