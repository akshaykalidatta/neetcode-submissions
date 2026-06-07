class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def rec(n):
            if n<=1:
                return cost[n]
            if n in dp:
                return dp[n]

            ans = cost[n] + min(rec(n-1), rec(n-2))
            dp[n] = ans
            return ans

        return min(rec(len(cost)-1), rec(len(cost)-2))