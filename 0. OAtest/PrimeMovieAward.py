def PrimeMoveAward(award, diff):
    award = sorted(award)
    min = float("-inf")
    cnt = 0
    for i in range(len(award)): 
        if min + diff > award[i]:
            continue
        else:
            min = award[i]
            cnt += 1
    
    return cnt

res = PrimeMoveAward([1,5,4,6,8,9,2], 3)
print(res)
