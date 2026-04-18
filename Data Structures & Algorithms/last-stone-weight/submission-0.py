class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heap = [-1*i for i in heap]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = (-1)*heapq.heappop(heap)
            y = (-1)*heapq.heappop(heap)

            if x == y:
                continue
            else:
                heapq.heappush(heap, (-1)*(x-y))

        return (-1)*heap[0] if len(heap)!=0 else 0     
