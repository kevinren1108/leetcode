from typing import List


def max_sub_array_len(nums: List[int], k: int) -> int:
    # Write your code here
    for i in range(1,len(nums)):
        nums[i] = nums[i] + nums[i-1]
    

    seen = {0:-1}
    maxLen = 0

    for i,n in enumerate(nums):
        diff = n - k
        if diff in seen:
            targetIndex = seen[diff]
            currLen = i - targetIndex 
            maxLen = max(maxLen, currLen)

        if n not in seen:
            seen[n] = i

    return maxLen

max_sub_array_len([1, -1, 5, -2, 3],3)