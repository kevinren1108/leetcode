#solution 1: sqrt root, O(sqrt(n))

def judgeSquareSum( c: int) -> bool:
    if c == 0:
        return True
    for i in range(0,int(sqrt(c))+1):
        bsq = c - i * i
        if bsq < 0:
            return False
        b = math.sqrt(bsq)
        if b == int(b):
            return True
    return False    

#two pointer:
def judgeSquareSum(self, c: int) -> bool:
    left = 0
    right = int(sqrt(c))
    while left <= right:
        cur = left * left + right * right
        if cur == c: return True
        if cur < c:
            left += 1
        else:
            right -= 1
    return False