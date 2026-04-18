# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = None
        def inorder(root):
            nonlocal ans, count
            if not root:
                return

            inorder(root.left)
            count += 1
            if count == k:
                ans = root.val
                return
            
            inorder(root.right)

        _ = inorder(root)
        return ans