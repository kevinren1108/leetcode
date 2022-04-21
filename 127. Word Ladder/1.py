
from collections import defaultdict, deque
from typing import List


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0
    
    nei = defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i + 1:]
            nei[pattern].append(word)
            
                
            
    visit = set([beginWord])
    q = deque([beginWord])
    res = 1
    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                for neiWord in nei[pattern]:
                    if neiWord not in visit:
                        visit.add(neiWord)
                        q.append(neiWord)
        res += 1
    return 0


ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])