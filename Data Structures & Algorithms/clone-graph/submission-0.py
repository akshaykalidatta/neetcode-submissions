"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None
        nodeMap = {}

        def dfs(node):
            if node in nodeMap:
                return nodeMap[node]

            newNode = Node(node.val)
            nodeMap[node] = newNode

            for i in node.neighbors:
                _ = dfs(i)
                newNode.neighbors.append(nodeMap[i])

            return newNode

        return dfs(node)