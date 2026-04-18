class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # dct = {}
        heap = []
        for i in range(len(points)):
            dist = math.sqrt((points[i][0])**2 + (points[i][1])**2)
            heapq.heappush(heap, (dist, (points[i][0], points[i][1])))
        ans = []
        while len(heap) > 0:
            dist, (i, j) = heapq.heappop(heap)
            ans.append(list((i, j)))
            if len(ans) == k:
                break

        return ans
