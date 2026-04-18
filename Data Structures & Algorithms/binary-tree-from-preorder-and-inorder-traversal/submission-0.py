# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i

        idx = 0
        def construct(left_idx, right_idx):
            nonlocal idx
            if left_idx > right_idx:
                return

            val = preorder[idx]
            idx += 1
            node = TreeNode(val)
            node.left = construct(left_idx, hashmap[val]-1)
            node.right = construct(hashmap[val]+1, right_idx)
            return node

        return construct(0, len(inorder) - 1)