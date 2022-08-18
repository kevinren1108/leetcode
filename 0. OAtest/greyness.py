def getMaximunGery(grid): 
    prfSumRow = [0]*len(grid) 
    prfSumCol = [0]*len(grid[0])
    for r in range(len(grid)): 
        for c in range(len(grid[0])): 
            if grid[r][c]=="1":
                prfSumRow[r]+=1; 
                prfSumCol[c]+=1 
            else:
                prfSumRow[r]-=1; 
                prfSumCol[c]-=1 
    return max(prfSumRow)+max(prfSumCol)

    