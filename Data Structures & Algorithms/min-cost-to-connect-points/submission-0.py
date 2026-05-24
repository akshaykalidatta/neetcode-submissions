class Solution:
    

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        rank = {}
        parent = {}
        for i in range(len(points)):
            rank[tuple(points[i])] = 1
            parent[tuple(points[i])] = tuple(points[i])

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return parent[node]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: return False
            if rank[p1]>rank[p2]:
                parent[p2] = p1
            elif rank[p1]<rank[p2]:
                parent[p1] = p2
            elif rank[p1]==rank[p2]:
                parent[p1] = p2
                rank[p2] += 1
            return True

        weights = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                heapq.heappush(weights, (dist, (x1, y1), (x2, y2)))

        mst = []
        ans = 0

        while weights and len(mst) <= len(points) - 1:
            wt, src, dst = heapq.heappop(weights)
            if not union(src, dst): continue
            ans += wt
            mst.append((src, dst))

        return ans



