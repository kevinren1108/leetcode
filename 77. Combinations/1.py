from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def backTracking(n,k,startIndex):
            if len(path) == k:
                ans.append(path.copy())
                return

            for i in range(startIndex, n+1):
                path.append(i)
                backTracking(n,k,i+1)
                path.pop()

        backTracking(n, k, 1)
        return ans

####optimaze
#https://www.bilibili.com/video/BV1ti4y1L7cv/?spm_id_from=333.788
def combine( n: int, k: int) -> List[List[int]]:
    ans = []
    path = []
    def backTracking(n,k,startIndex):
        if len(path) == k:
            ans.append(path.copy())
            return
        
        for i in range(startIndex, n-(k-len(path))+2):
            path.append(i)
            backTracking(n,k,i+1)
            path.pop()

    backTracking(n, k, 1)
    return ans

