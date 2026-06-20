class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][len(t)] = 1
        for i in range(len(t)):
            dp[len(s)][i] = 0

        for i in range(len(s)-1, -1, -1):
            for j in range(len(t)-1, -1, -1):
                skip = dp[i+1][j]
                if s[i]==t[j]:
                    take = dp[i+1][j+1]
                    skip+=take
                dp[i][j] = skip

        return dp[0][0]
        