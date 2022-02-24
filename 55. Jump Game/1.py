def canJump(self, nums: List[int]) -> bool:
             
        mostFar = 0
        goal = len(nums) - 1
    
        for i in range(len(nums)):
            if i <= mostFar:
                mostFar = max(mostFar, i + nums[i])
                if mostFar >= goal:
                    return True
        return False

