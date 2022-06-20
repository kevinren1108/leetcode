
def numSquares(n: int) -> int:
    print(dfs(n, 1, [], []))

def dfs(n, i, c, r):
    if n == 0:
        r += [c]
        return r
    
    elif n < 0 or i * i > n:
        return 
    
    dfs(n - i * i, i + 1, c + [i * i], r)
    dfs(n - i * i, i, c + [i * i], r)
    
    return r
        

numSquares(12)