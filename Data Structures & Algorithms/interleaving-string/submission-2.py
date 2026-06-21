class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False

        dp = [[-1]*(len(s2)+1) for _ in range(len(s1)+1)]
        def rec(i, j):
            if (i+j) == len(s3):
                return True
            # if i == len(s1) and j == len(s2):
            #     return False
            if dp[i][j] != -1:
                return dp[i][j]

            ans = False
            if i!=len(s1) and s1[i]==s3[i+j]:
                ans = rec(i+1, j)
            if j!=len(s2) and s2[j]==s3[i+j]:
                ans = ans or rec(i, j+1)

            dp[i][j] = ans
            return ans

        return rec(0, 0)