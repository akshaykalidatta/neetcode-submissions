# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def height(root: Optional[TreeNode]) -> int:
            nonlocal ans
            if not root:
                return 0
            hleft = height(root.left)
            hright = height(root.right)
            ans = max(hleft + hright, ans)
            return max(hleft, hright) + 1

        _ = height(root)
        return ans 