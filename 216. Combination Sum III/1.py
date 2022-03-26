
from typing import List


def combinationSum3( k: int, n: int) -> List[List[int]]:
    return dfs(k, n, 1, [], [])
    
def dfs( k, n, start, path, res):
    if n == 0 and len(path) == 3:
        res.append(path.copy())
        return
    
    if n < 0 or len(path) > 3 or start > 9:
        return
    
    for i in range(start, 10):
        path += [start]
        dfs(k, n - start, start + 1, path, res)
        path.pop()
        
    return res
        

combinationSum3(3,7)