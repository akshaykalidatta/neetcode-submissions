class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        set1 = set()
        for i in nums:
            set1.add(i)

        ans, starts = 0, []

        for i in range(len(nums)):
            temp = 0
            if nums[i]-1 not in set1:
                while nums[i] in set1:
                    temp +=1
                    nums[i] +=1
                ans = max(ans, temp)

        return ans
