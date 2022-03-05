def findMin(nums: List[int]) -> int:
#         [3,4,5,1,2]
#          l.  m.  r    
#         we have l , r , mid 
#         if r < mid, we know that the right potion is rotated. 
#         so we shoud update our left pointer, and tring to find the result on the right hand side
#         [6,7,1,2,3,4]
#          l.    m.  r
#         in the other case 
#         we have r < mid and l > mid:
#         Than we are sure that the target number is on the left hand side.
#         then we update our right pointer and tring search the target on the left side
        
#         we should wait l >= r happen, at that time, the left pointer should point to the targetdsaf