def sortArray(arr):
    return sorted(arr, key = lambda x:(x[1],~x[0]), reverse = True)

    return arr

res = sortArray([[1,3],[2,7],[2,5],[3,7],[1,7]])
print(res)
# [2,7],[3,7],[2,5],[1,3]


