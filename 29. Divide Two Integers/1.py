def divide(dividend: int, divisor: int) -> int:
    neg = 0
    if dividend < 0:
        dividend = -dividend
        neg += 1
    if divisor < 0:
        divisor = -divisor
        neg += 1
        
    cnt = 0   
    while dividend >= divisor:
        tmp = divisor
        mul = 1
        while dividend >= tmp:
            dividend -= tmp
            cnt += mul
            mul += mul
            tmp += tmp
        
    if neg == 1:
        cnt = -cnt
        
    return min(2147483647,max(-2147483648,cnt))
    
    
    # neg = 1 ans = -ans

divide(999,4)