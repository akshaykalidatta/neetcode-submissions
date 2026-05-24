class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ans = [0]*(n+1)
        adj = {}
        minHeap = []
        visited = set()

        for i in range(1, n+1):
            adj[i] = []

        for src, dst, wt in times:
            adj[src].append((dst, wt))

        heapq.heappush(minHeap, (0, k))
        while minHeap:
            wt, dst = heapq.heappop(minHeap)
            if dst in visited:
                continue
            ans[dst] = wt
            visited.add(dst)
            
            for n1, w1 in adj[dst]:
                if n1 not in visited:
                    heapq.heappush(minHeap, (wt+w1, n1))

        cnt = 0
        for i in ans:
            if i == 0: cnt+=1
            if cnt > 2: return -1
        return max(ans)

        