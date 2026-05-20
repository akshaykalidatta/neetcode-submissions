class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for src, dst in prerequisites:
            if src not in adj:
                adj[src] = []
            adj[src].append(dst)

        visited = set()
        def cycle(node) -> bool:
            if node not in adj:
                return False
            if node in visited: return True
            
            visited.add(node)
            for j in adj[node]:
                if cycle(j):
                    return True
            visited.remove(node)
            return False

        for i in adj:
            if cycle(i):
                return False

        return True