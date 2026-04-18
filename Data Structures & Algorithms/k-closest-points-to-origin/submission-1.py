class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        for i in range(len(points)):
            dist = math.sqrt((points[i][0])**2 + (points[i][1])**2)
            heapq.heappush(heap, ((-1)*dist, (points[i][0], points[i][1])))
            if len(heap) > k:
                heapq.heappop(heap)
            
        return ([list(x[1]) for x in heap])
