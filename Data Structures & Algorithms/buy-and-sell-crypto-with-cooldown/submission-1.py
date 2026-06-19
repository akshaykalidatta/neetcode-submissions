class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[float('-inf')]*2 for _ in range(len(prices)+1)]
        dp[len(prices)-1][1] = prices[-1]
        dp[len(prices)][0] = dp[len(prices)][1] = dp[len(prices)-1][0] = 0
        
        for i in range(len(prices)-2, -1, -1):
            dp[i][0] = max(dp[i+1][1]-prices[i], dp[i+1][0])
            dp[i][1] = max(dp[i+2][0]+prices[i], dp[i+1][1])

        return dp[0][False]