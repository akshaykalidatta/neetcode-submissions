# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root: TreeNode, curr_max):
            nonlocal count
            if not root:
                return
            if curr_max <= root.val:
                count += 1
            if root.left: 
                dfs(root.left, max(curr_max, root.left.val))
            if root.right:
                dfs(root.right, max(curr_max, root.right.val))

        _ = dfs(root, root.val)
        return count