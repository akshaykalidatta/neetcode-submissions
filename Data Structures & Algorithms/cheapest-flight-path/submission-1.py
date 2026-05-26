class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        cost = [INF]*n
        cost[src] = 0

        for i in range(k+1):
            temp = cost.copy()
            for s,d,w in flights:
                if w + cost[s] < temp[d]:
                    temp[d] = w + cost[s]

            cost = temp

        return cost[dst] if cost[dst] != INF else -1
