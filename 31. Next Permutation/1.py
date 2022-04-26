from typing import List

def dfs(nums, path, res):
    if not nums:
        res += [path.copy()]
        
        return res
    
    for i in range(len(nums)):
        path += [nums[i]]
        dfs((nums[:i] + nums[i+1:]), path, res)
    
    return res

def nextPermutation( nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(dfs(nums, [], []))
        

nextPermutation([1,2,3])

