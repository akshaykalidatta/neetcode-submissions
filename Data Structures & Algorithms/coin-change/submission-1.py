class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = {}
        def rec(amt):
            res = float('inf')
            if amt == 0:
                return 0
            if amt < 0:
                return -1
            if amt in dp:
                return dp[amt]

            for i in coins:
                temp = rec(amt-i)
                ans = (1 + temp) if temp>=0 else -1
                if ans == -1:
                    continue
                if ans < res:
                    res = ans

            dp[amt] = res if res!=float('inf') else -1

            return dp[amt] if amt in dp else -1

        return rec(amount)