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

    return mx

res = Maximum_K_Subarray([7,3,6,1], 2)
print(res)