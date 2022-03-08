
from typing import List


def lengthOfLIS(nums: List[int]) -> int:
        ans = 1
        curr = nums[len(nums)-1]
        for i in range(len(nums)-1,0,-1):
             
            if curr > nums[i-1]:
                ans += 1
                curr = nums[i-1]
        
        
        return ans

lengthOfLIS([4,10,4,3,8,9])