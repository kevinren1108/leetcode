from typing import List

def search(nums: List[int], target: int) -> int: 
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            
            # [4,5,6,7,0,1,2] mid = 7 l = 4 mid >= l 左半边是已经排序好的，
            # 因此，
            # 1.如果目标大于中位数，则目标在中位数右边，右半截数组，
            # 2.如果目标小于数组头，则目标并不在左边，在右边。
            # 这两种情况，都需要去左边搜索，所以让起始指针去到中位数右侧+1
            # 如果不符合这两种情况，则可以确定目标就在左侧， 因为 nums[l] < target < nums[mid]
            # 所以，我们把结束指针移动到中位数减一处。
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # [5,6,7,0,1,2,4] t = 2
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return -1


search([5,6,7,0,1,2,4],2)   