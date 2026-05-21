class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for j in adj[node]:
                if j == parent:
                    continue
                if not dfs(j, node):
                    return False
            return True

        if not dfs(0, -1) or len(visited) != n:
            return False
        
        return True