class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1]*(len(word2)+1) for _ in range(len(word1)+1)]

        for i in range(len(word1)+1):
            dp[i][len(word2)] = len(word1) - i
        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2) - j
        dp[len(word1)][len(word2)] = 0

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i]!=word2[j]:
                    delete = 1+dp[i+1][j]
                    insert = 1+dp[i][j+1]
                    replace = 1+dp[i+1][j+1]
                    ans = min(delete, insert, replace)
                else:
                    ans = dp[i+1][j+1]

                dp[i][j] = ans

        return dp[0][0]