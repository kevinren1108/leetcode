
def summaryRanges(nums):
    ranges = []
    ans = []
    for n in nums:
        if not ranges or n > ranges[-1][-1] + 1:
            ranges.append([])
        ranges[-1].append(n)
    
    for arr in ranges:
        if len(arr) == 1:
            ans.append(str(arr[0]))
        else:
            ans.append(str(arr[0])+"->"+str(arr[-1]))

    return ans
summaryRanges([0,2,3,4,6,8,9])

# 遍历input中的所有数字， 按照下列方法把结果加入暂存，
#     1. 如果暂存中没有层数，或当前层的最后一个数字小于当前数字减1，则新建一层。
#         如：ranges = [] （无当前层）
#             n = 9 ranges = [[1,2,3],[5,6]]  当前数：9 - 1 > 6 当前层最大数
#             ranges = [[1,2,3],[5,6]，[9]]
#     2. 如果当前层的最后一个数字等于当前数字减1，则证明当前数字和当前层最后一数字连续。
#             n = 7 ranges = [[1,2,3],[5,6]]  当前数：7 - 1 == 6 当前层最大数
#             ranges = [[1,2,3],[5,6,7]]

#     当循环结束时，输出每一层的头尾即可。