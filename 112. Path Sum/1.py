class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional


def dfs(root, path, res):
    if not root:
        return []
    
    path += [str(root.val)]
    
    if not root.left and not root.right:
        res.append(path.)
        path.pop()
        return res
    
    dfs(root.left, path, res)
    dfs(root.right, path, res)
    path.pop()
    
    return res

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    print(dfs(root,[],[]))


a = TreeNode(5,TreeNode(4,TreeNode(11,TreeNode(7,None,None),TreeNode(2,None,None))),TreeNode(8,TreeNode(13,None,None),TreeNode(4,None,TreeNode(1,None,None))))

hasPathSum(a, 22)