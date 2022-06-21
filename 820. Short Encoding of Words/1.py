from collections import defaultdict
from typing import List, Optional


class Node:
    def __init__(self, val: Optional[str]='#'):
        self.val = val
        self.children = defaultdict(Node)

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        curr = self.root
        word = word[::-1]
        for c in word:
            curr.val = c
            curr = curr.children[Node(c)]
            

    def count(self):
        return self.dfs(self.root, [], [])
        
    def dfs(self, root, path, res):
        if not root:
            return []
        
        if not root.children:
            res.append(path.copy())
            
            return res
        
        path += [root.val]
        for each in root.children:
            self.dfs(each, path, res)
        path.pop()
        
        return res
        

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        tree = Trie()
        for w in words:
            tree.insert(w)
        print(tree.count()) 
        

x = Solution()
x.minimumLengthEncoding(["time", "me", "bell"])