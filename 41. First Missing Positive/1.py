def firstMissingPositive(self, nums: List[int]) -> int:
    #solution 1 time O(n) space O(n)
#         val=set(nums)
#         for i in range(1,len(nums)+2):
        
#             if i not in val and i>0:
#                 return i

    #solution 2 time O(n) space O(1)
    # for the solution, we can use brust force: arrange each number to it index in the array, 
    # eg. [3,4,-1,1] -> [0,1,0,3,4] 
    # when we find the first 0, the conspoding index plus one will be the answer, in this case, it is 2
    # this will request o(n) spcae, how can we achieve a O(1) space?
    # we can sort this array in itself. so the space will be constants
    
    for i in range(len(nums)):
        while nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
            t = nums[i] - 1
            nums[i], nums[t] = nums[t], nums[i]


            
    print(nums)