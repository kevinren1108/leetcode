def Maximum_K_Subarray(arr, k):
    sm = sum(arr)
    mx = float("-inf")
    curr = 0
    for i in range(k - 1):
        curr += arr[i]

    for i in range(k-1, len(arr)):
        curr += arr[i]
        mx = max(mx, curr)
        curr -= arr[i-k+1]

    return sm - mx

res = Maximum_K_Subarray([7,3,6,1], 4)
print(res)
res = Maximum_K_Subarray([1,4,4,6,9,4], 2)
print(res)
res = Maximum_K_Subarray([10,4,8,1], 2)
print(res)
res = Maximum_K_Subarray([1,2,3,8,9,4,5], 2)
print(res)