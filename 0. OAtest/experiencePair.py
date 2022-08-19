def expPair(expe):
    myS = set()
    expe = sorted(expe)
    l = 0
    r = len(expe) - 1
    while l < r:
        average = (expe[l] + expe[r]) / 2
        myS.add(average)
        l += 1
        r -= 1

    return len(myS)

res = expPair([1,4,1,3,5,6])
print(res)
res = expPair([1,1,1,1])
print(res)