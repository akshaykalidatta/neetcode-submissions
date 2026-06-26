class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals = sorted(intervals, key= lambda x:x[0])
        ans.append(intervals[0])

        for i in range(1, len(intervals)):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(intervals[i][1], ans[-1][1]) 
            else:
                ans.append(intervals[i])

        return ans

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0: return [newInterval]
        if newInterval[0] <= intervals[0][0]:
            intervals.insert(0, newInterval)

        if newInterval[0] >= intervals[-1][0]:
            intervals.append(newInterval) 

        for i in range(1,len(intervals)):
            if newInterval[0] >= intervals[i-1][0] and newInterval[0] <= intervals[i][0]:
                intervals.insert(i, newInterval)

        return self.merge(intervals)