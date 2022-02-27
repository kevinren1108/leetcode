def jump(self, nums: List[int]) -> int:
    n = len(nums)
    
    l = 0    # l and r repesent the left side and right side of our bucket
    r = 0
    maxRight = nums[0]
    
    step = 0
    
    while r < n-1:
        print(l,r)
        for i in range(l,r+1):
            maxRight = max(maxRight, i+ nums[i]) # 2(0+2),4(1+3),8(4+4)
        l = r + 1
        r = maxRight
        
        step += 1
        
    return step

# we have to think it in a step process like a bucket.
# Say we have a nums : [2,3,1,1,4] 
#the first bucket is when we stand initially [2] ,which is two
#                                            l r   where l = r = 0
#in this bucket, we know our maxmen far is 0 + 2(current index + most far) 
# so we have new bucket [3,1]
#                        l r   where l = 1 and r = 2
#in this bucket, we know our maxmen far is 1 + 3(current index + most far) 
# so we have new bucket [1,4]
#                        l r   where l = 3 and r = 4

#at r = 4, we reach the goal of the jump game. So we set up our while loop 
#condition is r < n - 1 where n is the length of nums.

#we have 3 bucket, first 1 is our begin, which is not count, 2nd and 3rd will
#be counted, so the total steps is 2 steps.