

from typing import List


# def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         candidates.sort()
#         dfs(candidates, target, 0, [], res)
#         return res
    
# def dfs(nums, target, index, path, res):
#     if target < 0:
#         return  # backtracking
#     if target == 0:
#         res.append(path)
#         return 
#     for i in range(index, len(nums)):
#         dfs(nums, target-nums[i], i, path+[nums[i]], res)


def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    print(self.dfs(candidates, target, 0, [], []))

def dfs(self, nums, target, startIndex, path, ans):
    if target == 0:
        ans.append(path.copy)
        return
    
    self.dfs(nums, target - nums[startIndex], startIndex, path, ans)
    
    self.dfs(nums, target - nums[startIndex], startIndex + 1, path, ans)
    
    return ans
    
combinationSum([2,3,6,7],7)