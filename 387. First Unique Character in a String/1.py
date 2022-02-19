def twoSum(self, nums: List[int], target: int) -> List[int]:
    numMap = dict() 
    for i in range(0,len(nums)):
        diff = target - nums[i]
        if diff in numMap:
            return [i,diff.value()]
        else:
            dict.add(nums[i],i)