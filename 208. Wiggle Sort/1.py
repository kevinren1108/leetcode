def wiggleSort(self, nums):
    # write your code here
    for i in range(1,len(nums)):
        if i % 2 == 1:
            if nums[i] < nums[i-1]:
                nums[i],nums[i-1] = nums[i-1],nums[i]
        if i % 2 == 0:
            if nums[i] > nums[i-1]:
                nums[i],nums[i-1] = nums[i-1],nums[i]