# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #height function
        ans = True
        def height(root: Optional[TreeNode]):
            nonlocal ans
            if not root:
                return 0
            hleft = height(root.left)
            hright = height(root.right)
            if abs(hleft - hright) > 1:
                ans = False
            return max(hleft, hright) + 1

        _ = height(root)
        return ans