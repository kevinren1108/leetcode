class Solution:
    def numDecodings(self, s: str) -> int:
        print(self.dfs(s, [], []))
        
    
    def dfs(self, s, path, res):
        if not s:
            res += [path.copy()]
        
        nextOne = s[:1]
        nextTwo = s[:2]
        print(nextOne, nextTwo)
        if int(nextOne) > 0:
            path += [nextOne]
            self.dfs(s[1:], path, res)
        if len(nextTwo) > 1 and int(nextTwo) <= 26:
            path += [nextTwo]
            self.dfs(s[2:], path, res)
        print(res)
        # if path:
        #     path.pop()
        return res
        
