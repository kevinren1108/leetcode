from typing import List


def removeDuplicates(nums: List[int]):
    if len(nums) <= 2:
         return nums
    
    slow = 2
    fast = 2
    
    while fast < len(nums):
        if nums[slow - 2] != nums[fast]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

            
    return slow


removeDuplicates([0,0,1,1,1,1,2,3,3])