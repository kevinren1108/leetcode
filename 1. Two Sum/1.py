def twoSum(self, nums: List[int], target: int) -> List[int]:
    myD = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in myD:
            return [i, myD[diff]]
        else:
            myD[nums[i]] = i