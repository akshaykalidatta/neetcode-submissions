class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key= lambda x:x[0])
        ans = 0
        prev = intervals[0]
        
        for i in range(1, len(intervals)):
            if prev[1] > intervals[i][0]:
                prev = prev if prev[1] <= intervals[i][1] else intervals[i]
                ans += 1
            else:
                prev[1] = intervals[i][1]

        return ans