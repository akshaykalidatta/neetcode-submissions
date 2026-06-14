class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [nums[-1], 0]
        i = len(nums)-2

        while i >= 0:
            tmp = dp[0]
            dp[0] = max(nums[i]+dp[1], dp[0])
            dp[1] = tmp
            i-=1

        return dp[0]
