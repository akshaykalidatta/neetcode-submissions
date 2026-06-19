class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1]*(len(text2)+1) for _ in range(len(text1)+1)]
        def rec(i, j):
            if i>=len(text1) or j>=len(text2):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            
            ans = 0
            if text1[i]==text2[j]:
                ans = 1 + rec(i+1,j+1)
            else:
                ans = max(rec(i+1, j), rec(i, j+1))
            dp[i][j] = ans

            return ans

        return rec(0, 0)