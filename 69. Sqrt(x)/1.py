def mySqrt(self, x: int) -> int:
    if x < 2: return x
    l = 1
    r = x - 1
    while l <= r:
        mid = int(l + (r - l) / 2)
        res = mid * mid
        if res == x:
            return mid
        elif res > x:
            r = mid - 1
        else:
            l = mid + 1
    return l - 1