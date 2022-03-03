#Greddy solution
def wiggleMaxLength(nums: List[int]) -> int:
    res = []
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            res += ["d"]
        elif nums[i] == nums[i+1]:
            res += ["e"]
        else:
            res += ["u"]

            
    if len(res) == 1 and res[0] == "e":
        return 1
    
    total = 1

    curr = "c"
    for i in range(0,len(res)):
        if not res[i] == curr and res[i] is not "e":
            total += 1
            curr = res[i]

    return total


#DP solution
def wiggleMaxLength(nums: List[int]) -> int:
    up,down = 1,1
    
    for i in range(0,len(nums)-1):
        if nums[i] > nums[i+1]:
            down = up + 1
        elif nums[i] < nums[i+1]:
            up = down + 1
            
    ans = max(up,down)
    
    return ans
    