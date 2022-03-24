class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findLeaves(root):
    ans = level(root, [])
    print(ans)
def level(root, ans):
    if not root:
        return -1

    left = level(root.left, ans)
    right = level(root.right, ans)
    
    height = 1 + max(left, right)
    if len(ans) <= height:
        ans.append([])
    ans[height] += [root.val]
    
    return height



a= TreeNode(1, TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3))

findLeaves(a)