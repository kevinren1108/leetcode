def getEncrNum(arr):
    if len(arr) == 1:
        return "0" + str(arr[0])

    if len(arr) == 2:
        return str(arr[0]) + str(arr[1])

    newArr = []

    for i in range(len(arr)-1):
        newArr += [(arr[i] + arr[i + 1]) % 10]
    
    return getEncrNum(newArr)

res = getEncrNum([4,5,6,7])
print(res)