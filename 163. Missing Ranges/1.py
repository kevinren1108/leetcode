def helper(left_point, right_point):
        if left_point == right_point:
            return str(left_point)
        else:
            return str(left_point) + "->" + str(right_point)
            
def findMissingRanges(nums, lower, upper):
    # write your code here
    ans = []
    if len(nums) == 0:
        ans.append(helper(lower, upper))
        return ans
    pre_point = lower - 1
    for point in nums:
        if pre_point != point and pre_point + 1 != point:
            ans.append(helper(pre_point + 1, point - 1))
        pre_point = point
    if nums[-1] < upper:
        ans.append(helper(nums[-1] + 1, upper))
    return ans
            