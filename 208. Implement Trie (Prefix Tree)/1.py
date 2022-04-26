from collections import defaultdict


class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.eow = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.eow = True

    def search(self, word: str) -> bool:
        self.res = False
        self.dfs(self.root, word, 0)
        return self.res
    
    def startsWith(self, prefix: str) -> bool:
        self.res = False
        self.dfs(self.root, prefix, 0, need_eow = False)
        return self.res
    
    def dfs(self, root, word, index, need_eow = True):
        if index >= len(word):
            if root.eow and need_eow:
                self.res = True
            if not need_eow:
                self.res = True
            return
        
        root = root.children.get(word[index])
        if not root:
            return
        self.dfs(root, word, index + 1)


x = Trie()
x.insert("apple")
x.startsWith("app")
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)