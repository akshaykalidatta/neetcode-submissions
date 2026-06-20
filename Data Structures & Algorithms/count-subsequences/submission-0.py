class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1]*len(t) for _ in range(len(s))]
        def rec(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]

            skip = rec(i+1, j)
            if s[i] == t[j]:
                take = rec(i+1, j+1)
                skip += take
            
            dp[i][j] = skip
            return dp[i][j]

        return rec(0,0)