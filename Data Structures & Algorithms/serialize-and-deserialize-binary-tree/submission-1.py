# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        ans = []
        def inorder(root):
            if not root:
                ans.append('N')
                return
            ans.append(str(root.val))
            inorder(root.left)
            inorder(root.right)

        inorder(root)
        return ','.join(ans)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "": return None
        data = data.split(',')
        idx = 0
        def dfs():
            nonlocal idx
            val = data[idx]
            idx += 1
            if val == 'N':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs() 
            return node 

        return dfs()
