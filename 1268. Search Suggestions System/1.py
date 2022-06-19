class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.words = []

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        curr = self.root
        for c in word:
            curr = curr.children[c]
            if len(curr.words) < 3:
                curr.words += [word]
    
    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children: 
                return ''
            curr = curr.children[c] 
        return curr.words
    
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        myTree = Trie()
        products = sorted(products)
        for w in products:
            myTree.insert(w)  
        curr = ""
        ans = []
        for c in searchWord:
            curr += c 
            ans.append(myTree.search(curr))
        return ans    
        
        