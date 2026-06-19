class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[float('-inf')]*2 for _ in range(len(prices))]
        print(dp)
        def rec(i, has):
            profit = 0
            if i > len(prices)-1:
                return 0
            if i == len(prices)-1 and has:
                return prices[i]
            if dp[i][has] != float('-inf'):
                return dp[i][has]            

            #buy
            if not has:
                profit = max(rec(i+1, True)-prices[i], rec(i+1, False))
            #sell
            elif has:
                profit = max(rec(i+2, False)+prices[i], rec(i+1, True))
            
            dp[i][has] = profit
            return dp[i][has]


        return rec(0, False)