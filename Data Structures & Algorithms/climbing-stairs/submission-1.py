class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        i = 2
        while i <= n:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            i+=1

        return dp[1]