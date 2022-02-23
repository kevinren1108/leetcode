def generate(self, numRows: int) -> List[List[int]]:
    n = numRows
    ans = [[1]*i for i in range(1,n+1)]
    for i in range(1,n):
        for k in range(1, i):
            ans[i][k] = ans[i-1][k] + ans[i-1][k-1]
            
    return ans