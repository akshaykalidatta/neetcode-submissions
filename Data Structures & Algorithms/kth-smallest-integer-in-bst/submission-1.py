# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 1
        ans = None
        def inorder(root):
            nonlocal ans, count
            if not root:
                return

            inorder(root.left)
            
            if count == k:
                ans = root.val

            count += 1
            
            inorder(root.right)

        _ = inorder(root)
        return ans