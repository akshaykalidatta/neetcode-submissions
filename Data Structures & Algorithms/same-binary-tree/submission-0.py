# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = True
        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]):
            nonlocal ans
            if not p and not q:
                return
            elif (p and not q) or (q and not p) or p.val != q.val:
                ans = False
            else:
                dfs(p.left, q.left)
                dfs(p.right, q.right)

        _ = dfs(p, q)
        return ans