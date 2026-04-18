class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set()
        for i in nums:
            numset.add(i)

        starts = set()
        for i in nums:
            if (i-1) not in numset:
                starts.add(i)

        ans = 0
        temp = 0
        for i in numset:
            if i in starts:
                j = i
                while j in numset:
                    temp += 1
                    j += 1

                ans = max(ans,temp)
                temp = 0

        return ans