#思路：
# l,r指代左右指针
# 在任意一点l或r上，只要lmax<rmax,这一点就可以有水，水的多少取决于lmax和rmax中小的一方（木桶效应）
# 这一点水的多少可以通过公示
#     某一点上水的量 = height[l or r] - 小的那个边界lmax or rmax 
# 算出，

# l，r可以分别指向头和尾，因为我们并不急于算出某个区间有多少水，而是专注于当前点上有多少水。
# 因此，当lmax<=rmax时，我们必定可知这一点上有水。有水的多少只是根据当前点高度和最低点高度的差值决定的
# 例如 [0，1，0，2]
# 在index 1这一点上，lmax = 1，rmax = 2， lmax<rmax, water = lmax - height[l] = 1 - 1 = 0
# 在index 2这一点上，lmax = 1, rmax = 2, lmax<rmax, water = lmax - height[l] = 1 - 0 = 1

def trap( height: List[int]) -> int:
    if len(height)<= 2:
        return 0
    
    ans = 0
    
    #using two pointers i and j on indices 1 and n-1
    l = 0
    r = len(height) - 1
    
    #initialising leftmax to the leftmost bar and rightmax to the rightmost bar
    lmax = height[l]
    rmax = height[r]
    
    
    # water level for index i = min(lmax,rmax) - height[i]
    
    while l < r:
        lmax = max(height[l], lmax)
        rmax = max(height[r], rmax)
        
        if lmax <= rmax:
            ans += lmax - height[l]
            l += 1
        else:
            ans += rmax - height[r]
            r -= 1
            
    return ans


    
    