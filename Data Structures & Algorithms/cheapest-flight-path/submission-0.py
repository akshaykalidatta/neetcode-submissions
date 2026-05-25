class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        heap = []
        visited = set()
        for i in range(n):
            adj[i] = []
        for s,d,w in flights:
            adj[s].append((d,w))

        heapq.heappush(heap, (0,-1,src))
        ans = 0
        while heap:
            wt, stop, d = heapq.heappop(heap)
            if stop > k or (d, stop) in visited: continue
            visited.add((d, stop))
            if d == dst: return wt

            for n,w in adj[d]:
                if (n, stop + 1) not in visited:
                    heapq.heappush(heap, (w+wt, stop+1, n))

        return -1
    