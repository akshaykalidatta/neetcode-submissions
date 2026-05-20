class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = {}
        adj = {}
        ans = []
        for i in range(numCourses):
            adj[i] = []
            indeg[i] = 0

        for src, dst in prerequisites:
            adj[src].append(dst)
            indeg[dst] += 1

        queue = deque()
        for i in indeg:
            if indeg[i] == 0:
                queue.append(i)

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                ans.append(node)
                for i in adj[node]:
                    if indeg[i] > 0:
                        indeg[i] -= 1
                    if indeg[i] == 0:
                        queue.append(i)
                    

        if len(ans) != numCourses: return []
        ans.reverse()
        return ans
