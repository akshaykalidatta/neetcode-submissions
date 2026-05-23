class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for src, dst in prerequisites:
            adj[src].append(dst)

        visited = set()
        path = set()
        def cycle(node) -> bool:
            if node in path: return True
            if node in visited: return False
            
            visited.add(node)
            path.add(node)
            for j in adj[node]:
                if cycle(j):
                    return True
            path.remove(node)
            # adj[node] = []
            return False

        for i in adj:
            if cycle(i):
                return False

        return True