
def maxArea(height: List[int]) -> int:
    maxWater = 0
    
    l = 0
    r = len(height) - 1
    
    while l < r:
        
        maxWater = max(maxWater,min(height[l],height[r])*(r-l))
        
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
            
    return maxWater