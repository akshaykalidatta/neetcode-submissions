"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x: x.start)
        ans = 1
        heap = [intervals[0].end]
        for i in range(1, len(intervals)):
            if heap and heap[0] <= intervals[i].start:
                heapq.heappop(heap)
                ans -= 1

            heapq.heappush(heap, intervals[i].end)
            ans += 1

        return ans