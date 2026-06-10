class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        i = 1
        while i < len(dp):
            for j in coins:
                if (i - j) >= 0:
                    dp[i] = min(dp[i], 1+dp[i-j])
            i+=1

        return dp[amount] if dp[amount]!=float('inf') else -1
