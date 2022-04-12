from math import inf
from typing import List

step = float(inf)

def oneDiff(curr, nxt) -> bool:
    if len(curr) != len(nxt):
        return False
    
    diff = 0
    for i in range(len(curr)):
        if curr[i] != nxt[i]:
            diff += 1
    
def dfs(bw, ew, lst, count):
    print(bw)
    if not bw or not ew or not lst:
        return 0

    if bw == ew:
        step = min(step, count)  
        return count
    
    for i in range(len(lst)):
        if oneDiff(bw, lst[i]):
            tmp = lst[i]
            newL = lst[:i] + lst[i+1:]
            dfs(tmp, ew, newL, count + 1)
    return count


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0
    
    dfs(beginWord, endWord, wordList, 1)
    print(step)
    
    
ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])