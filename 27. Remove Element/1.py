def removeElement(self, nums: List[int], val: int) -> int:
    slow = 0
    fast = 0
    count = 0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            fast += 1
            slow += 1
            count += 1
        else:
            fast += 1
    return count