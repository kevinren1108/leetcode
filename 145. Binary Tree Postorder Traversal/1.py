def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    
    return self.dfs(root,result)

def dfs(self, root, res):
    if root == None:
        return res
    
    self.dfs(root.left, res)
    self.dfs(root.right, res)
    res += [root.val]
    
    return res