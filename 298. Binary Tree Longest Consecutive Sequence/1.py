class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def longest_consecutive(root: TreeNode) -> int:
    ans = 0
    def dfs(root, size, preNum):
        if not root:
            return 

        if root.val == preNum + 1:
            size += 1
        else:
            size = 1
        
        ans = max(ans,size)

        dfs(root.left, size, root.val)
        dfs(root.right, size, root.val)

        return size

    
    if not root:
        return 0
    else:
        dfs(root, 0, root.val)
    print(ans)

#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5

a = TreeNode(1,None,TreeNode(3,TreeNode(2,None,None),TreeNode(4,None,TreeNode(5))))

longest_consecutive(a)