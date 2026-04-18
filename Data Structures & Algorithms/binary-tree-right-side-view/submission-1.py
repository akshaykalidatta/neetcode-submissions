# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #similar to before only push the last one
        if not root: return []
        q = deque()
        q.append(root)
        ans = []
        while len(q)!=0:
            subans = []
            length = len(q)
            while length!=0:
                curr = q.popleft()
                subans.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                length -= 1

            ans.append(subans[-1])

        return ans

        