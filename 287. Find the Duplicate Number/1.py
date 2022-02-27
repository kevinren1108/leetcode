from collections import Counter
from typing import List

def findDuplicate(nums: List[int]) -> int:
    numSet = Counter(nums)
    return numSet.most_common(1)[0][0]


def findDuplicate(nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[nums[0]]
    finder = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
        
    slow = 0
    
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow
        
        

findDuplicate([3,1,3,4,2])