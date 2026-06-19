class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1]*(amount+1) for _ in range(len(coins)+1)]
        def rec(i, rem):
            if i >= len(coins):
                return 0
            if rem==0:
                return 1
            if rem<0:
                return 0
            if dp[i][rem]!=-1:
                return dp[i][rem]

            ans = rec(i+1, rem)
            if rem >= coins[i]:
                take = rec(i, rem-coins[i])
                ans += take

            dp[i][rem] = ans

            return dp[i][rem]

        return rec(0, amount)