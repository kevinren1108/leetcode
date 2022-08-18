def add(curr, k):
    curr = set(curr)
    res = 0
    for i in range(len(curr), k):
        for j in range(1, 1000):
            if j in curr:
                continue
            else:
                curr.add(j)
                res += j
                break

    return res

res = add([6,8,3,5], 7)
print(res)