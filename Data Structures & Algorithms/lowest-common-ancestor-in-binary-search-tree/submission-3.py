# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path1 = []
        path2 = []
        def dfs(root: Optional["TreeNode"], target: int, path: List["TreeNode"]) -> None:
            if not root:
                return
            path.append(root)
            if root.val < target:
                dfs(root.right, target, path)
            elif root.val > target:
                dfs(root.left, target, path)
        
        dfs(root, p.val, path1)
        dfs(root, q.val, path2)

        ancestor = root
        for node in path1:
            if node in path2:
                ancestor = node

        return ancestor
