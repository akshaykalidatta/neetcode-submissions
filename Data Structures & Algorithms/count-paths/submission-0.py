class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]
        def rec(i, j):
            if i>m-1 or j>n-1:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if  i==m-1 or j==n-1:
                return 1

            ans = rec(i+1, j) + rec(i, j+1)
            dp[i][j] = ans
            return ans
            

        return rec(0, 0)