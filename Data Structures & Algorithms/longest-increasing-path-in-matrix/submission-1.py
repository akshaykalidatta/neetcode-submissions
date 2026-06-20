class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[-1]*(len(matrix[0])) for _ in range(len(matrix))]
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def rec(r, c):
            if dp[r][c] != -1:
                return dp[r][c]

            ans = -1
            for dr, dc in directions:
                if (r+dr) < 0 or (c+dc) < 0 or (r+dr) >= len(matrix) or (c+dc) >= len(matrix[0]) or matrix[r+dr][c+dc] <= matrix[r][c]:
                    continue
                ans = max(ans, rec(r+dr, c+dc))
            if ans == -1:
                dp[r][c] = 1
                return 1

            dp[r][c] = ans + 1
            return dp[r][c]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                _ = rec(i, j)

        res = -1
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                res = max(res, dp[i][j])

        return res
