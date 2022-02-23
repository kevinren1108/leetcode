def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    #first solution time:O(n) space: O(n)
#         a = [0] * len(nums)
#         for i in range(len(nums)):
#             a[(i+k)% len(nums)] = nums[i]
        
#         for i in range(len(nums)):
#             nums[i] = a[i]
        

    #second solution time: O(n) space: O(1)
    def revers(nums: List[int], start: int, end: int) -> List[int]:
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
    
    k %= len(nums)
    revers(nums,0,len(nums)-1)    #  7 6 5 4 3 2 1
    revers(nums,0,k-1)            #  5 6 7 4 3 2 1
    revers(nums,k,len(nums)-1)    #  5 6 7 1 2 3 4