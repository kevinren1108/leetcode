def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    
    return self.dfs(root, result)

def dfs(self, root, res):
    if root == None:
        return res
    
    res += [root.val]
    self.dfs(root.left, res)
    self.dfs(root.right, res)
    return res


