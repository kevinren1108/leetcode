def guessNumber(self, n: int) -> int:
    l = 1
    r = n 
    while l < r:
        mid = l + (r-l) // 2           
        if guess(mid) == 1:
            l = mid + 1
        else:
            r = mid 
    return l
            