def share(categories, k):
    res = 0
    for i in range(1, len(categories)):
        pS = set(categories[:i])
        sS = set(categories[i:])
        cnt = 0
        for item in pS:
            if item in sS:
                cnt += 1
        if cnt > k:
            res += 1
    return res

res = share("adbccdbada", 2)
print(res)