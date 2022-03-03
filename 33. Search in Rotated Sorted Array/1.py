from typing import List


def search(nums: List[int], target: int) -> int:
    
    
    l = 0
    r = len(nums) - 1
    
    
    
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # [5,6,7,0,1,2,4] t = 2
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        
    return -1


search([5,6,7,0,1,2,4],2)   