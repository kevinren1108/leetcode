def getMaxValue(arr):
    arr.sort()
    if arr[0] != 1 :
        arr[0] = 1
    for i in range(1 , len(arr)):
        if  abs(arr[i-1] - arr[i]) <= 1 :
            continue
        else :
            arr[i] = arr[i-1] + 1     
    return max(arr)

res = getMaxValue([2,2,1,2,1])
print(res)