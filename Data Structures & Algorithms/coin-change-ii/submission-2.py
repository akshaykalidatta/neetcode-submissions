class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1]*(amount+1) for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 1
        for i in range(1, amount+1):
            dp[len(coins)][i] = 0

        for i in range(len(coins)-1, -1, -1):
            for j in range(1,amount+1):
                ans = dp[i+1][j]
                if j>=coins[i]:
                    take = dp[i][j-coins[i]]
                    ans += take
                dp[i][j] = ans
        
        return dp[0][amount]