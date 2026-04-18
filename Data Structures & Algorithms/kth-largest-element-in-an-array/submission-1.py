class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # heapq.heapify(heap)

        for i in nums:
            heapq.heappush(heap, i)
            while len(heap) > k:
                heapq.heappop(heap)

        return heap[0]