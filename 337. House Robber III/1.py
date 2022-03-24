from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rob(root: Optional[TreeNode]) -> int:
    
    globalMax = float('-inf')
    
    def dfs(root):
        if not root:
            return 0

        leftMax = max(dfs(root.left), 0)
        rightMax = max(dfs(root.right), 0)
        print(leftMax, rightMax, "root.val: ", root.val)
        globalMax += max(globalMax, root.val, leftMax + rightMax)
        
        
        return root.val
    
    dfs(root)
    return (globalMax)

a = TreeNode(3,TreeNode(2,None,3),TreeNode(3,None,1))
rob(a)