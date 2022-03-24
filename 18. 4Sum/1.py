from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    if len(nums) < 4:
        return []
    
    nums = sorted(nums)
    # [-2,-1,0,0,1,2]
    ans = []
    
    for i in range(len(nums)):
        j = i + 1
        while j < len(nums):
            
            l = j + 1
            r = len(nums) - 1
            
            newTar = target - nums[i] - nums[j]
            
            while l < r:
                total = nums[l] + nums[r]
                
                if total == newTar:
                    ans += [[nums[i],nums[j],nums[l],nums[r]]]
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif total < newTar:
                    l += 1
                else:
                    r -= 1
            
            j += 1
            while j < len(nums) and nums[j] == nums[j-1] :
                j += 1
            
    return ans

fourSum([2,2,2,2,2], 8)