class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        ans = 0
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for j in adj[node]:
                if j not in visited:
                    dfs(j)
            return

        for i in range(n):
            if i not in visited and len(visited)!=n:
                ans+=1
                dfs(i)

        return ans