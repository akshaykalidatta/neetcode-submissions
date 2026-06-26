class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        qu = [[queries[i], i] for i in range(len(queries))]
        qu = sorted(qu, key= lambda x:x[0])
        intervals = sorted(intervals, key=lambda x:x[0])
        ans = [-1]*(len(queries))

        heap = []
        j = 0
        for q, i in qu:
            while j < len(intervals) and intervals[j][0] <= q:
                heapq.heappush(heap, ((intervals[j][1]-intervals[j][0]+1), intervals[j][1]))
                j+=1

            while heap and q > heap[0][1]:
                heapq.heappop(heap)
            
            ans[i] = heap[0][0] if heap else -1

        return ans
