# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(self, root):
            if not root:
                return 0
            
            left = dfs(self, root.left)
            right = dfs(self, root.right)
            diameter = left + right
            self.res = max(self.res, diameter)
            return max(left + 1, right + 1)
        
        dfs(self, root)

        return self.res