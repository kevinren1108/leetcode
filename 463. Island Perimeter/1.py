from typing import List

def islandPerimeter(grid: List[List[int]]) -> int:
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                
                print(dfs(grid, i, j, perimeter))
    return perimeter
    

def dfs(grid, r, c, perimeter):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "#":
        return (False, 0)
    
    if grid[r][c] == 0:
        return (False, 0)
    
    grid[r][c] = "#"
    
    temp = 4
    state, val = dfs(grid, r + 1, c, perimeter + temp)
    if state:
        temp -= 1
    state, val = dfs(grid, r - 1, c, perimeter + temp)
    if state:
        temp -= 1
    state, val = dfs(grid, r, c + 1, perimeter + temp)
    if state:
        temp -= 1
    state, val = dfs(grid, r, c - 1, perimeter + temp)
    if state:
        temp -= 1
        
    return (True, temp + perimeter)
    
islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])