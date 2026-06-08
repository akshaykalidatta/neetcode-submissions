class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def rec(n):
            if n == len(nums)-1:
                return nums[n]
            if n > len(nums)-1:
                return 0

            if n in dp:
                return dp[n]

            ans = max(nums[n] + rec(n+2), rec(n+1))
            dp[n] = ans
            return ans

        return rec(0)