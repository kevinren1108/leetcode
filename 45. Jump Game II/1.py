from typing import List
   
def jump( nums: List[int]) -> int:
        jump = curEnd = curFar = 0
        l = len(nums)
        
        for i in range(l-1):
            curFar = max(curFar, i+nums[i])
            if curEnd == i:
                jump += 1
                curEnd = curFar
        return jump

jump([3,1,2,1,4])