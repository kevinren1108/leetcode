def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    bucket = [0] * 3
    
    for n in nums:
        bucket[n] += 1
        
    print(bucket)
    
    pos = 0    
    for i in range(0,len(nums)):
        while pos < 2 and bucket[pos] == 0:
            pos += 1
        if bucket[pos] > 0:
            nums[i] = pos
            bucket[pos] -= 1