def Aggregate_Temperature_Chnage(tempChange):
    right = sum(tempChange)
    left = 0
    mx = float("-inf")
    res = []
    for i in range(len(tempChange)):
        left += tempChange[i]
        mx = max(mx, max(left, right))
        right -= tempChange[i]
    return mx

res = Aggregate_Temperature_Chnage([6,-2,5])
print(res)


