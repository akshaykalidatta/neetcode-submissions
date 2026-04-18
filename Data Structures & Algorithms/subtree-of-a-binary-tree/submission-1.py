# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]):
            if not p and not q:
                return True
            if (p and not q) or (q and not p) or (p.val!=q.val):
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def dfs(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            if not root:
                return False
            if isSameTree(root, subRoot):
                return True
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)

        return dfs(root, subRoot)

        
            
