class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1]*(len(word2)+1) for _ in range(len(word1)+1)]
        def rec(i, j):
            if j == len(word2) and i==len(word1):
                return 0
            if j == len(word2):
                return len(word1)-i
            if i == len(word1):
                return len(word2)-j
            
            if dp[i][j]!=-1:
                return dp[i][j]

            if word1[i]==word2[j]:
                ans = rec(i+1, j+1)
            elif word1[i]!=word2[j]:
                delete = 1 + rec(i+1, j)
                insert = 1 + rec(i, j+1)
                replace = 1 + rec(i+1,j+1)
                ans = min(delete, insert, replace)

            dp[i][j] = ans
            return ans
        
        return rec(0, 0)