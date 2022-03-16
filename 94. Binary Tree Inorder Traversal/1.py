def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    
    return self.dfs(root, result)

def dfs(self, root, res):
    
    if root == None:
        return res
            
    self.dfs(root.left, res)
    res += [root.val]
    self.dfs(root.right, res)    
    
    return res