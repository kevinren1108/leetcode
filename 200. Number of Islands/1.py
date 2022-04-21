from typing import List


def numIslands(grid: List[List[str]]) -> int:
    res = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                res += 1 if dfs(grid, r, c) else 0
    return res
    
def dfs(grid, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
        return False
    
    if grid[r][c] == "0":
        return False
    
    dfs(grid, r + 1, c)
    dfs(grid, r - 1, c)
    dfs(grid, r, c + 1)
    dfs(grid, r, c - 1)
    
    if grid[r][c] == "1":
        grid[r][c] = "#"
        return True
