def minimenSumArray(arr, k):
    sm = sum(arr)
    curr = 0
    for i in range(k-1):
        curr += arr[i]
    mx = float("-inf")
    for i in range(k-1, len(arr)):
        curr += arr[i]

        mx = max(mx, curr)

        curr -= arr[i - k + 1]

    return sm - mx

res = minimenSumArray([10,4,8,13,20], 2)
print(res)
res = minimenSumArray([4,6,10,8,2,1], 3)
print(res)