class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def rec(x):
            if x <= 1:
                return 1
            if x in dp:
                return dp[x]
            ans = rec(x-1) + rec(x-2)
            dp[x] = ans
            return ans

        return rec(n)
