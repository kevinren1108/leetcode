def searchRange(self, nums: List[int], target: int) -> List[int]:   
    if not nums: return [-1,-1]
    def searchLow(nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) 
        while(l < r):
            mid = int(l + (r-l)/ 2)
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l
    
    def searchHigh(nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) 
        while(l < r):
            mid = int((l + r)  / 2)
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l
    
    low = searchLow(nums,target)
    high = searchHigh(nums,target)-1
    if low == len(nums)  or nums[low] != target:
        return [-1,-1]
    return[low,high]
