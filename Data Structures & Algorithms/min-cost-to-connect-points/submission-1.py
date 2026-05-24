class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        heap = []
        heapq.heappush(heap, (0, 0))
        ans = 0

        while heap and len(visited) != len(points):
            wt, node = heapq.heappop(heap)
            if node in visited: continue
            visited.add(node)
            ans += wt
            for j in range(len(points)):
                if j not in visited:
                    x1, y1 = points[node]
                    x2, y2 = points[j]
                    dist = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(heap, (dist, j))

        return ans