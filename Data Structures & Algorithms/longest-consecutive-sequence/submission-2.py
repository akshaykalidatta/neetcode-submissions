class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        set1 = set()
        for i in nums:
            set1.add(i)

        ans, starts = 1, []

        for i in range(len(nums)):
            temp = 0
            start = nums[i]-1
            if (nums[i]-1) not in set1:
                while (start+1) in set1:
                    temp +=1
                    start +=1
                else:
                    ans = max(ans, temp)
                    temp = 1
                    continue

        return ans
